# Contributing

You do not need to be a programmer. The most useful contributions come from people who do medical-legal work.

## The one rule: invented data only

**Never post real patient or case information here.** That means issues, pull requests, test cases, screenshots, and pasted AI output.

- No real names, dates of birth, claim numbers, employers, providers, or records.
- No "lightly edited" real documents. Changing a name does not make a record safe.
- Write a fictional case that shows the same problem instead.

Everything in this repository is public. If you see real information posted here, report it privately. See [`SECURITY.md`](./SECURITY.md).

## Ways to help

- **Tell us what happened when you used a skill.** What tool you used, what worked, what didn't.
- **Report a failure.** A skill that misses a conflict, invents a value, cites something that is not in the source, or overstates what it checked.
- **Send a fictional test case** that exposes a failure.
- **Propose a skill.** One job, a clear input and output, a clear line where the physician decides, and a way to test it.

Open an issue with the matching template. For anything short, the Feedback button on [qmeaihero.com](https://qmeaihero.com) also works.

## Changing a skill

A skill changes only for a reason we can test.

1. Show the failure with a fictional case.
2. Make the smallest change to `SKILL.md` that fixes it.
3. Say how you tested it, and in which AI tool.
4. Say whether the change moves a safety boundary: what the skill will assert, what it leaves for the physician, what it refuses to do.

We may hold a change until we have run it against our test cases.

## Before you open a pull request

```
python3 scripts/check_repo.py
```

This checks the skill frontmatter, that each download in `docs/` matches its source folder, and that links resolve. If you changed a skill, rebuild its download first:

```
scripts/build-skill-zip.sh <skill-name>
```

Changes reach `main` only through a pull request.

## Style

Short sentences. Plain words. No em dashes.
