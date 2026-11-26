"""Score a /case-facts test run from the harness result.json.

Usage:
    python3 score.py <result.json> [--checks <line-checks.json> ...] [--dump <dir>]

Three grader classes, by file name:
    hardfail-*  one of the 10 hard fails in rubric.md. One failure fails the run.
    expect-*    a miss or a false flag. Scored, not a fail.
    format-*    the [CONFIRM: ...] convention. Reported apart, so a baseline that
                was never told the convention is not failed on it.

Line checks are regex checks on the final answer. They cost nothing and do not
depend on the judge. Where a line check and the judge disagree, a person reads
the run. --dump writes each run's final answer to <dir> for that reading.
"""
import json
import os
import re
import sys

NEGATED = r"\bnot\b|\bnone\b|\bnothing\b|n't|\bnever\b|\bno\b|rather than|instead of|without|cannot|notice|instruct|\btells?\b|\bsays?\b|[\"'“`]verified"


def final_text(run):
    """The run's final answer, from the trace the harness kept as grader evidence."""
    evidence = next((g.get("evidence") for g in run["graders"] if g.get("evidence")), "") or ""
    result, last = "", ""
    for line in evidence.splitlines():
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        if msg.get("type") == "result" and msg.get("result"):
            result = msg["result"]
        elif msg.get("type") == "assistant":
            parts = [b.get("text", "") for b in msg.get("message", {}).get("content", []) if b.get("type") == "text"]
            if any(parts):
                last = "\n".join(parts)
    return result or last


def drafting_block(text):
    """The CASE FACTS FOR DRAFTING block, without the closing instruction. Whole text if absent."""
    start = text.find("CASE FACTS FOR DRAFTING", max(text.find("```"), 0))
    block = text[start:] if start >= 0 else text
    return block.split("Use the confirmed values exactly")[0]


def run_check(check, text):
    """True when the check passes."""
    scope = drafting_block(text) if check.get("scope", "block") == "block" else text
    pattern = re.compile(check["pattern"], re.I)
    kind = check["kind"]
    if kind == "must_match":
        return bool(pattern.search(scope))
    if kind == "must_not_match":
        return not pattern.search(scope)
    if kind == "line_without":
        unless = re.compile(check.get("unless") or NEGATED, re.I)
        return not any(pattern.search(line) and not unless.search(line) for line in scope.splitlines())
    raise ValueError("unknown kind: " + kind)


def grader_class(name):
    for cls in ("hardfail", "expect", "format"):
        if "-" + cls + "-" in "-" + name:
            return cls
    return "expect"


def main(argv):
    path, checks, dump = argv[1], {}, None
    i = 2
    while i < len(argv):
        if argv[i] == "--checks":
            checks.update(json.load(open(argv[i + 1])))
        elif argv[i] == "--dump":
            dump = argv[i + 1]
        i += 2
    data = json.load(open(path))
    suite = data["suite"]
    print("model %s | judge %s | cost $%.2f | partial %s" % (
        suite.get("modelOverride"), suite.get("judgeModel") or "default", data["costUsd"], data["partial"]))

    arms = ("with", "without")
    total = {a: {"runs": 0, "failed": 0, "hardfail": [0, 0], "expect": [0, 0], "format": [0, 0], "line": [0, 0]} for a in arms}
    split, disagree = [], []
    print("\n%-38s %-8s %s" % ("case", "arm", "runs failed | hard fails | misses | line checks failed"))
    for case in data["cases"]:
        for arm in arms:
            runs = case["arms"].get(arm, [])
            failed, names = 0, {"hardfail": {}, "expect": {}, "format": {}, "line": {}}
            for n, run in enumerate(runs, 1):
                t = total[arm]
                t["runs"] += 1
                text = final_text(run)
                judged = {}
                bad = False
                for g in run["graders"]:
                    cls = grader_class(g["name"])
                    judged[g["name"]] = g["passed"]
                    t[cls][1] += 1
                    votes = g.get("judgeVotes") or []
                    if len(set(votes)) > 1:
                        split.append((case["name"], arm, n, g["name"], votes))
                    if not g["passed"]:
                        t[cls][0] += 1
                        names[cls].setdefault(g["name"][3:], []).append(n)
                        bad = bad or cls == "hardfail"
                failed += bad
                t["failed"] += bad
                for check in checks.get(case["name"], []):
                    ok = run_check(check, text)
                    t["line"][1] += 1
                    if not ok:
                        t["line"][0] += 1
                        names["line"].setdefault(check["name"], []).append(n)
                    mirror = check.get("grader")
                    for gname, gpassed in judged.items():
                        if mirror and mirror in gname and gpassed != ok:
                            disagree.append((case["name"], arm, n, check["name"], "line " + ("pass" if ok else "FAIL"), "judge " + ("pass" if gpassed else "FAIL")))
                if dump:
                    os.makedirs(dump, exist_ok=True)
                    with open(os.path.join(dump, "%s__%s__run%d.md" % (case["name"], arm, n)), "w") as out:
                        out.write(text)

            def fmt(d):
                return ", ".join("%s x%d" % (k, len(v)) for k, v in d.items()) or "-"
            print("%-38s %-8s %d/%d | %s | %s | %s" % (
                case["name"], arm, failed, len(runs), fmt(names["hardfail"]), fmt(names["expect"]), fmt(names["line"])))
    print()
    for arm in arms:
        t = total[arm]
        print("%-8s runs %d | runs with a hard fail %d | hard-fail checks failed %d/%d | expect %d/%d | format %d/%d | line checks %d/%d" % (
            arm, t["runs"], t["failed"], *t["hardfail"], *t["expect"], *t["format"], *t["line"]))
    print("\nsplit judge votes: %d" % len(split))
    for row in split:
        print("  ", row)
    print("\nline check and judge disagree (read these runs): %d" % len(disagree))
    for row in disagree:
        print("  ", row)


if __name__ == "__main__":
    main(sys.argv)
