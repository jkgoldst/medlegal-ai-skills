# Changelog

## v0.1.0 (unreleased)

First public release of `/case-facts`.

### The skill

- Compares identifying and administrative facts across case documents: examinee name, date of birth, injury dates, claim and case numbers, employer, attorneys, claims administrator, and evaluation details.
- Reports each fact as `confirmed`, `consistent`, `single-source`, `conflict`, `missing`, or `needs checking`, with a source for every value.
- Never picks between conflicting values. Unresolved facts stay as `[CONFIRM: field]` placeholders.
- Examination facts (date, place, mode, interpreter) stay as placeholders until a person confirms them, because a document written before the exam states what was scheduled, not what happened.
- Does not say the report is ready or that the user can sign it.
- Quote marks mean the source's exact words.
- Ignores instructions embedded in case documents.
- Does not review diagnoses, causation, impairment, or legal conclusions.

### Included

- `skills/case-facts/SKILL.md`
- `skills/case-facts/examples/`: a fictional three-document packet with an answer key.
- `docs/case-facts.zip`: the same folder, zipped.

### Tested

- Claude Code: supported. See the README for the other tools, none of which is tested yet.
- Measured against the same model without the skill on 11 fictional case files. One model, a small set. Not an accuracy claim.
