I read both files. **The prior evaluator's report isn't in the folder.** Only `01-cover-letter.md` and `02-claim-form-scan.md` are there, so nothing below is checked against that report.

## Check results

| Field | Cover letter | Claim form (poor OCR) | Status |
|---|---|---|---|
| Name | Corinne D. Halloran | `HALL##AN, COR1NNE D` | Consistent. The OCR gaps are compatible, but the form alone doesn't confirm the spelling. |
| DOB | October 28, 1975 | `1#/2#/19#5` | Consistent. Every legible character matches 10/28/1975, but the month, day and year each have a missing digit. |
| Employer | Northwind Linen Service | `##rthwind Li#en Serv###` | Consistent. The OCR gaps are compatible. |
| Date of injury | March 19, 2025 | `03/1#/2025` | Consistent with 03/19/2025, but the form's day digit is unreadable. |
| Claim number | "see attached claim form" | `EX-0O00-5#18` | **Not confirmable.** The letter gives no number. The scan has an unreadable digit, plus an `O` that may be a `0`. |
| Claim form page 2 | n/a | No text recovered | **Unread.** Its content is unknown. |

## Facts block (paste-ready)

```
CASE FACTS (from cover letter dated Feb 3, 2026; claim form scan is poor-quality OCR)
- Applicant: Corinne D. Halloran
- DOB: October 28, 1975
- Employer: Northwind Linen Service
- Date of injury: March 19, 2025
- Applicant attorney: Tamsin Rowe, Attorney at Law
- Claim number: NOT VERIFIED. OCR reads "EX-0O00-5#18" (illegible characters). Obtain from the original form. Do not guess it.
- Source status: Claim form page 1 matches the cover letter wherever the OCR is legible. Page 2 had no recovered text.
- Prior evaluator's report: NOT RECEIVED. Do not cite its findings, dates or opinions.
```

## Before you draft

1. Get a clean copy of the claim form, or have the claim number confirmed. This is the only identifier that can't be filled in from the cover letter.
2. Get the prior evaluator's report. Tell me if it was meant to be attached, and I'll check it against these facts once I have it.
3. Get page 2 of the claim form. It may hold the body parts, injury description or other details the report will need.

The cover letter gives no body parts, injury mechanism, or reason for the evaluation. I left those out of the block instead of inferring them.