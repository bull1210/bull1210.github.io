Drop Search Console exports here (Performance > Search results > Export > Download CSV gives a zip with
Queries.csv and Pages.csv; the zip itself or Queries.csv both work). Name them by date, e.g. `2026-11-30.zip`.
`python tools/seo/gaps.py` reads every file; the newest number per query wins.
