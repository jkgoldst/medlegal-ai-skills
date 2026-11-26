# MedLegal AI Hero: AI Skills for Medical-Legal Work

Free, practical AI skills for physicians doing medical-legal work. Use them with the AI tools you already have, or build your own workflows.

Site: **[qmeaihero.com](https://qmeaihero.com)**

Each skill is a set of reusable instructions that teaches an AI tool one medical-legal task. The skills follow the open [Agent Skills specification](https://agentskills.io/specification): a folder with a `SKILL.md`. The skills keep evidence traceable, uncertainty visible, and medical judgment with the physician.

> **Public-good project:** the skills in this repository are meant to be useful on their own. They are not tied to any commercial application.

## New to AI in medical-legal work?

Read **[Start Here: Set Up AI for Medical-Legal Work](https://qmeaihero.com/start-here.html)** first. It covers choosing an AI environment, what to check before using real records, and trying your first skill on a fictional case.

## Skill #1: `/case-facts`

**Catch conflicting facts before they make it into the report.**

[`/case-facts`](./skills/case-facts/SKILL.md) checks identifying and administrative facts across your case documents: examinee name, date of birth, injury dates, claim and case numbers, employer, attorneys, and other parties. It shows what agrees, what conflicts, and what's missing, with the source for every value.

It never picks between conflicting values for you. Unresolved facts stay as visible placeholders, such as `[CONFIRM: date of birth]`, rather than being guessed.

It does not review diagnoses, causation, impairment, or legal conclusions.

Page: [qmeaihero.com/case-facts.html](https://qmeaihero.com/case-facts.html)

### Try it on a fictional case first

[`skills/case-facts/examples/`](./skills/case-facts/examples/) holds a fictional three-document packet (cover letter, records summary, interview excerpt) and an answer key listing what a correct run should report and what counts as a failure. No real patient information.

### Install

| Tool | Status | How |
| --- | --- | --- |
| Claude Code | **Supported.** Tested 2026-11-26 | Copy [`skills/case-facts`](./skills/case-facts/) into `.claude/skills/` in your project folder (or `~/.claude/skills/` to have it everywhere), then type `/case-facts`. A plain request such as "check my case for inconsistent identifying information" also starts it. It reads PDFs and text files. |
| Claude (claude.ai) | Not tested yet | Download [`case-facts.zip`](./docs/case-facts.zip) and upload it under *Settings → Capabilities → Skills*. |
| ChatGPT for Clinicians and other chat products | Not tested yet | Attach `SKILL.md` with your documents and ask the AI to follow it. |
| Codex and other agents that read skill folders | Not tested yet | Copy the folder into the agent's skills folder. |

Please open an issue with what worked and what didn't.

### How it was tested, and the limits

- **The tests are public.** [`evals/case-facts/`](./evals/case-facts/) holds the rules, 8 of the test cases with answer keys, the scoring tools, and the results, including where the skill failed. Three more cases are held out so that a fix is judged on cases it was not built on.
- We ran the skill and the same model without it on 11 fictional case files, three times each. Each run was checked against a written list of 10 failures that matter, such as an invented value, a silent choice between conflicting sources, or a quote that is not in the source.
- The model without the skill most often failed by calling facts "verified", by reporting scheduled exam details as if the exam had happened that way, and by telling the physician the report could be signed.
- One model was tested (Claude Sonnet), on a small set of invented files. These are engineering checks, not an accuracy claim. Other models may behave differently.
- The skill checks identifying and administrative facts only. Read its output as a list of things to check, not as clearance to sign.

**Only use real patient records in an AI environment authorized for protected health information.** The skill provides no HIPAA compliance or security controls. If you can't establish that your setup is authorized, use fictional case files.

## More skills coming

Records review, report critique, deposition preparation, and other reusable workflows.

## How these skills work

**Small and composable.** Each skill does one medical-legal job well rather than owning the whole workflow.

**Evidence first.** Important claims trace back to source material.

**Uncertainty stays visible.** Unknown does not become "probably fine." An unresolved fact is better than a plausible invention.

**Physician controlled.** AI can read, organize, compare, and flag. The physician owns interpretation, medical judgment, and the final report.

**Tested, not just polished.** A skill is judged by whether it catches what it should and never invents what it shouldn't, not by whether its output looks good.

**Open.** Inspect them, fork them, adapt them, and improve them.

## What this project does not do

This project does **not**:

- certify that an environment is HIPAA compliant or secure
- provide legal or compliance advice
- guarantee an accurate report
- make medical-legal conclusions on behalf of a physician

## Repository structure

```text
medlegal-ai-skills/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/                    # the site (GitHub Pages) and downloadable skill zips
├── scripts/
│   ├── build-skill-zip.sh   # builds docs/<skill>.zip
│   └── check_repo.py        # frontmatter, zips match source, links resolve
├── skills/
│   ├── case-facts/
│   │   ├── SKILL.md
│   │   └── examples/        # fictional packet and answer key
│   └── qme-env-audit/       # earlier skill, not currently featured
└── evals/
    ├── case-facts/          # rules, test cases, scoring tools, results
    └── qme-env-audit/
```

## Contributing

This project is early. The most useful contributions:

- feedback from physicians doing medical-legal work
- fictional test cases that expose failure modes
- corrections where a skill overstates what an AI system can verify
- proposals for small, reusable skills with a clear input, output, physician decision boundary, and evaluation method

**Invented data only.** Never post real patient or case information in an issue, a pull request, or a test case. Everything here is public.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). To report a security or safety problem privately, see [`SECURITY.md`](./SECURITY.md).

## License

MIT. See [`LICENSE`](./LICENSE).
