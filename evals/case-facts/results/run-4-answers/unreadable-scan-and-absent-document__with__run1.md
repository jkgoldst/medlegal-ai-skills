# Case facts check

**Sources reviewed:** 01-cover-letter.md (applicant attorney's letter, Feb 3, 2026); 02-claim-form-scan.md (OCR of claim form).
**Coverage limits:** You mentioned a prior evaluator's report, but it wasn't in the input files and I couldn't find it in the directory. It was not reviewed. The claim form OCR is poor, and page 2 recovered no text. Cross-source checks cover only the cover letter against the claim form, and the claim form is mostly unreadable.

## Needs attention

1. **Claim number: MISSING (unusable)**
   - Cover letter: "Claim number: see attached claim form"
   - Claim form OCR: "Cla1m No: EX-0O00-5#18". Several characters are masked or ambiguous (`O` vs `0`, `#`).
   - Why it matters: the number can't be reliably read from either source.
   - Next: Get the number from the original claim form image or from the claims administrator.
   - Drafting value: [CONFIRM: claim number]

2. **Date of injury: NEEDS CHECKING**
   - Cover letter: "March 19, 2025"
   - Claim form OCR: "03/1#/2025". The day digit is unreadable. The `1` is partly legible, and the second digit is masked.
   - This is compatible with the cover letter but doesn't confirm it. I can't tell whether the claim form says 19, and I haven't filled in the masked digit.
   - Next: Check the original claim form image.
   - Drafting value: [CONFIRM: date of injury]. The cover letter value, "March 19, 2025", is single-source, and I'd treat it as unverified.

3. **Date of birth: NEEDS CHECKING**
   - Cover letter: "October 28, 1975"
   - Claim form OCR: "1#/2#/19#5". Month, day, and year digits are partly masked. The visible digits don't contradict the cover letter, but they also can't corroborate it.
   - Next: Check the original claim form or ID.
   - Drafting value: [CONFIRM: date of birth]. The cover letter value is single-source and unverified.

4. **Examinee name: NEEDS CHECKING**
   - Cover letter: "Corinne D. Halloran"
   - Claim form OCR: "HALL##AN, COR1NNE D". The masked characters and the `1` in place of `i` are probably OCR damage. The surname has the right length and endpoints for "Halloran", but I can't confirm that from the scan.
   - Next: Check the original claim form.
   - Drafting value: "Corinne D. Halloran" (single-source, unverified), or [CONFIRM: examinee name] if you prefer to hold it.

## Facts at a glance
| Fact | Status | Value / issue | Evidence |
| --- | --- | --- | --- |
| Examinee name | Needs checking | Cover letter clear; scan partly masked | Cover letter "Re:" line; claim form "Emp1oyee nam" |
| Date of birth | Needs checking | Scan masked | Cover letter; claim form "D.O.B." |
| Date of injury | Needs checking | Day digit masked on scan | Cover letter; claim form "Date of 1njury" |
| Claim number | Missing | Unreadable | Claim form "Cla1m No" |
| Employer | Needs checking | Cover letter: "Northwind Linen Service". Scan: "##rthwind Li#en Serv###". Probably compatible but masked. | Cover letter; claim form "Emp1oyer" |
| Applicant attorney | Single-source | Tamsin Rowe, Attorney at Law | Cover letter letterhead |
| Defense attorney, claims administrator | Missing | Not stated | none |
| Evaluation date, location, mode, interpreter | Missing | Not stated | none |
| Prior evaluation date | Missing | The prior report wasn't provided | none |

## Questions for the reviewer
1. Can you share the prior evaluator's report, which didn't come through? It's the only likely second clean source for the name, DOB, injury date, and claim number.
2. Can you supply a clean copy of the claim form, or read the masked fields yourself?
3. Who is the claims administrator and defense counsel?

## Case facts for drafting

**CONFIRMED:** none.

**CONSISTENT BUT UNVERIFIED:** none. The scan is too degraded to establish agreement.

**SINGLE-SOURCE / NEEDS CHECKING** (cover letter only; do not present as verified):
- Examinee: Corinne D. Halloran
- Date of birth: October 28, 1975
- Date of injury: March 19, 2025 (one event; no cumulative-trauma range stated)
- Employer: Northwind Linen Service
- Applicant attorney: Tamsin Rowe, Attorney at Law

**UNRESOLVED:**
- Claim number: [CONFIRM: claim number]. The scan reads "EX-0O00-5#18", which is unreliable.
- Defense attorney: [CONFIRM: defense attorney]
- Claims administrator: [CONFIRM: claims administrator]
- Evaluation date, location, mode, interpreter: [CONFIRM: field]
- Report date and signing county: [CONFIRM: field]

> Use the confirmed values exactly as provided for identifying and administrative facts. Do not replace them with conflicting values found elsewhere in the records. You may use a consistent or single-source claim fact exactly as cited, but do not describe it as confirmed. Leave examination facts, physician-only facts, and unresolved facts as `[CONFIRM: field]` and flag them for human review. Preserve source-attributed accounts as accounts rather than established facts.

This check covers identifying and administrative facts only. It makes no judgment on whether the report is ready.