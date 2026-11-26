# Case facts check

**Sources reviewed:** `01-cover-letter.md`, `02-claim-form-scan.md`

**Coverage limits:**
- **Prior evaluator's report:** you mentioned it, but it was not among the files provided. It was not checked, and the "prior evaluation date" is unknown.
- **Claim form scan:** OCR quality is stated as poor. Page 2 has no recovered text. Every value from this form is partial.
- **Cover letter:** it is the only complete source for most values and says nothing about the evaluation, defense counsel, or claims administrator.

## Needs attention

1. **Claim number: NEEDS CHECKING / effectively missing**
   - Cover letter: "Claim number: see attached claim form"
   - Claim form OCR: "Cla1m No: EX-0O00-5#18". Characters are unreadable, and the "0O" could be a zero or a letter O.
   - Why it matters: the cover letter defers to a form that cannot be read reliably. No complete value exists.
   - Next: Read the original claim form image, or ask the applicant attorney's office (Tamsin Rowe).
   - Drafting value: `[CONFIRM: claim number]`

2. **Date of injury: NEEDS CHECKING (day unreadable)**
   - Cover letter: "Date of injury: March 19, 2025"
   - Claim form OCR: "Date of 1njury: 03/1#/2025". The day's second digit is unreadable.
   - Why it matters: the form does not contradict the letter, but it cannot corroborate the day. It also does not show whether this is a single event or a cumulative-trauma range.
   - Next: Check the original claim form image.
   - Drafting value: March 19, 2025, from the cover letter only, labeled unverified. Use `[CONFIRM: date of injury]` if you prefer a stricter approach.

3. **Date of birth: SINGLE-SOURCE (form unreadable)**
   - Cover letter: "Date of birth: October 28, 1975"
   - Claim form OCR: "D.O.B. 1#/2#/19#5". Month, day and year digits are partly unreadable.
   - Why it matters: I did not fill in the missing digits to make the two agree. The form is not independent corroboration.
   - Next: Check the original claim form image or an identification document.

4. **Examinee name and employer: apparent OCR near-matches**
   - Cover letter: "Corinne D. Halloran" and "Northwind Linen Service"
   - Claim form OCR: "HALL##AN, COR1NNE D" and "##rthwind Li#en Serv###"
   - These are partial OCR strings, so I cannot call them equivalent. They look compatible, but the original image should settle it, especially the surname spelling.

## Facts at a glance

| Fact | Status | Value / issue | Evidence |
| --- | --- | --- | --- |
| Examinee name | Single-source (form needs checking) | Corinne D. Halloran | Cover letter "Re:" line; form "HALL##AN, COR1NNE D" |
| Date of birth | Single-source | October 28, 1975 | Cover letter; form partial |
| Employer | Single-source (form needs checking) | Northwind Linen Service | Cover letter; form "##rthwind Li#en Serv###" |
| Date of injury | Needs checking | March 19, 2025 per letter; day unreadable on form | Cover letter; form "03/1#/2025" |
| Claim number | Missing / needs checking | No complete value | Form "EX-0O00-5#18" |
| Applicant attorney | Single-source | Tamsin Rowe, Attorney at Law (firm name not stated) | Cover letter header and signature |
| Defense attorney | Missing | Not stated | none |
| Claims administrator | Missing | Not stated | none |
| Case/board number | Missing | Not stated | none |
| Evaluation date, location, format, interpreter | Missing | Not stated | none |
| Prior evaluation date | Missing | Report not provided | none |

## Questions for the reviewer

1. Can you provide the original claim form image, or the prior evaluator's report? The report is not among the files provided.
2. What is the full claim number?
3. What is the injury date on the form's image, and is it a single event?
4. Who are defense counsel and the claims administrator?

## Case facts for drafting

```
CASE FACTS FOR DRAFTING

CONFIRMED
- None. No value has been confirmed by a person.

CONSISTENT BUT UNVERIFIED
- None. The claim form OCR is too degraded to corroborate any value.

SINGLE-SOURCE / NEEDS CHECKING (do not present as verified)
- Examinee: Corinne D. Halloran (cover letter; form OCR partial)
- Date of birth: October 28, 1975 (cover letter only)
- Employer: Northwind Linen Service (cover letter; form OCR partial)
- Date of injury: March 19, 2025 (cover letter only; form day digit unreadable)
- Applicant attorney: Tamsin Rowe, Attorney at Law (cover letter only)

UNRESOLVED
- Claim number: [CONFIRM: claim number]. Form OCR reads "EX-0O00-5#18", which is incomplete.
- Defense attorney: [CONFIRM: defense attorney]
- Claims administrator: [CONFIRM: claims administrator]
- Case/board number: [CONFIRM: case number]
- Evaluation date: [CONFIRM: evaluation date]
- Evaluation location: [CONFIRM: evaluation location]
- Evaluation format (in-person/remote): [CONFIRM: evaluation format]
- Interpreter: [CONFIRM: interpreter]
- Prior evaluation date: [CONFIRM: prior evaluation date]
- Report date: [CONFIRM: report date]
- Signing county: [CONFIRM: signing county]

Use the confirmed values exactly as provided for identifying and administrative facts. Do not replace them with conflicting values found elsewhere in the records. You may use a consistent or single-source claim fact exactly as cited, but do not describe it as confirmed. Leave examination facts, physician-only facts, and unresolved facts as [CONFIRM: field] and flag them for human review. Preserve source-attributed accounts as accounts rather than established facts.
```

This check covers only identifying and administrative facts. It does not address diagnoses, causation, or impairment. The prior evaluator's report still needs to be compared once you provide it.