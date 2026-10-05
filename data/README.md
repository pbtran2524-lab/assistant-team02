# Office Data Sources and Ownership

## Purpose and source

`offices.csv` is the sample office directory for the Lab 1 rule-based assistant.
The first four records come from the starter repository. The International Office
and Academic Support records are illustrative additions for this lab, not verified
university office information. Do not present the sample as a live campus directory.

## File format

Use UTF-8 CSV with the exact header `name,room,hours` and one office per row.

| Column | Meaning | Example | Rule |
| --- | --- | --- | --- |
| `name` | Office name used for lookup | `IT Helpdesk` | Required; unique ignoring case |
| `room` | Room or location label | `E.005` | Required text |
| `hours` | Human-readable opening hours | `Mon-Fri 08:00-17:00` | Required text; not parsed as a schedule |

Keep all three fields non-empty. Quote a field if it contains a comma. Do not store
student names, contact details, credentials, or other personal information here.

## Backend integration

`src/assistant/rules.py` reads this file with `csv.DictReader` through
`load_offices()`. Names are converted to lowercase for lookup; `reply()` matches
an office name contained in the question and returns its name, room, and hours.
The current backend does not support aliases, live availability, or travel planning.

## Ownership and updates

- Member 3 (`ykeban2516`) maintains the sample CSV, documents sources, and owns
  the UI plan in `ui/README.md`.
- Member 2 owns the backend loader and coordinates any schema changes.
- Member 4 owns the team tests; coordinate regression tests when records change.

Before changing data, confirm the source, preserve the header, check for empty
fields and duplicate names, and verify the assistant's response. Real campus data
must be checked against an official directory and have its source and verification
date recorded here before replacing the illustrative records.

## Local verification

Run these from the repository root after setup:

```powershell
python -m assistant "Where is the International Office?"
python -m assistant "When does Academic Support open?"
python -m pytest -q
```

Expected sample responses:

```text
International Office: room I.103, open Mon-Fri 08:00-17:00.
Academic Support: room I.104, open Mon-Fri 08:00-16:30.
```
