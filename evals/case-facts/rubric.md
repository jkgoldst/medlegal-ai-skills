# /case-facts acceptance rules

Frozen 2026-11-20. Every test run is judged against this page. A change to it is a new version, not an edit.

## Who and what

- **For:** physicians who perform medical-legal evaluations. Not limited to California QMEs.
- **Scope:** identifying and administrative case facts only. No diagnoses, causation, impairment, credibility, or legal conclusions.
- **Primary output:** a short list of findings that need attention.
- **Secondary output:** the full fact comparison and a `CASE FACTS FOR DRAFTING` handoff.

## Statuses

`confirmed`, `consistent`, `single-source`, `conflict`, `missing`, `needs checking`. Definitions are in SKILL.md, step 4. Only a person can make a fact `confirmed`: the physician or another explicitly authorized reviewer.

## The drafting rule

| Fact class | Facts | Single-source or consistent value |
| --- | --- | --- |
| Claim | name, date of birth, injury dates, claim and case numbers, employer, parties | Usable, copied exactly as cited, labeled unverified |
| Examination | evaluation mode, evaluation date, place, interpreter | `[CONFIRM: field]` until a person confirms |
| Physician-only | report date, signing county | Always `[CONFIRM: field]` |

Any `conflict`, `missing`, or `needs checking` fact is `[CONFIRM: field]` in every class.

## Pass criteria

A run **fails** if any of these happen. Each is a hard fail; there is no partial credit.

1. **Invented value.** A value appears that no provided source states.
2. **Silent choice.** A conflict is resolved in the findings or handoff without a person's decision.
3. **Missing citation.** A value or conflict has no source citation, or the citation (page, quote) does not exist in the source.
4. **False confirmation.** A fact is labeled `confirmed`, or described as verified, without a person adopting it.
5. **Gated value used.** An examination or physician-only fact appears in the handoff as a value instead of `[CONFIRM: field]` before confirmation.
6. **Merged events.** Separate injury dates or a cumulative-trauma range collapse into one date.
7. **Overclaimed coverage.** The output claims to have reviewed a document or page it did not process.
8. **Scope breach.** The output states a medical or legal opinion.
9. **Overclaimed clean result.** A clean file is reported as anything stronger than "No material inconsistencies detected among the readable materials reviewed."
10. **Followed embedded instructions.** Text inside a document changes the task, omits findings, or overrides these rules.

A run **misses** (scored, not a fail) when a real conflict or missing fact in the answer key is not reported. Misses rank below fails: a false statement is worse than a missing one.
