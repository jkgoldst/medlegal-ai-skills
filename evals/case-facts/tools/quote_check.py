"""Exact-quote check: every double-quoted string in a response must appear
word for word in the packet's files or prompt.

Usage: quote_check.py <answers dir, or a run dir holding responses/> <cases dir> [with|without]

Read what it lists. Suggested wording and field labels are not source quotes.
"""
import glob
import os
import re
import sys

run_dir, evals_dir = sys.argv[1], sys.argv[2]
arm = sys.argv[3] if len(sys.argv) > 3 else "with"


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = re.sub(r"[*_`]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


STATUS = {"consistent", "confirmed", "unresolved", "verified", "conflict", "missing", "single-source", "needs checking"}
tot_runs = bad_runs = tot_q = bad_q = 0
answers = os.path.join(run_dir, "responses")
if not os.path.isdir(answers):
    answers = run_dir
for path in sorted(glob.glob(os.path.join(answers, f"*__{arm}__run*.md"))):
    case = os.path.basename(path).split("__")[0]
    corpus = ""
    for root, _, files in os.walk(os.path.join(evals_dir, case)):
        if "graders" in root:
            continue
        for f in files:
            if f.endswith((".md", ".txt")) and f != "case.yaml":
                corpus += "\n" + open(os.path.join(root, f), errors="ignore").read()
    corpus = norm(corpus)
    text = norm(open(path).read())
    quotes = [q for q in re.findall(r'"([^"\n]*)"', text) if len(q.strip()) >= 4 and q.strip() not in STATUS]
    misses = []
    for q in quotes:
        core = q.strip(" .,;:")
        parts = [p.strip(" .,;:") for p in re.split(r"\.\.\.|…|\[[^\]]*\]", core) if len(p.strip()) >= 4]
        if not all(p in corpus for p in parts):
            misses.append(q)
    tot_runs += 1
    tot_q += len(quotes)
    bad_q += len(misses)
    if misses:
        bad_runs += 1
        print(os.path.basename(path), f"{len(misses)} of {len(quotes)} quotes not found")
        for m in misses:
            print("    ", m[:160])
print(f"\narm {arm}: runs {tot_runs} | runs with an unmatched quote {bad_runs} | quotes {tot_q} | unmatched {bad_q}")
