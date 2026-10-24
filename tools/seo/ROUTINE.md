# Weekly guide routine (the brief for the scheduled agent)

You maintain the PixOrg guides site, repo `bull1210/bull1210.github.io`, branch `main`, built by GitHub Pages.
You run once a week. You never publish directly: your output is at most one pull request.

## Each run

1. Clone the repo. Read `STYLE.md`. List `_guides/` so you know what exists.
2. Get this week's Search Console data: a new file in `data/gsc/` (the owner drops the export there) or, when
   the `GSC_CREDENTIALS` secret exists, the Search Console API for the last 28 days written to
   `data/gsc/<today>.csv` with the columns Top queries, Clicks, Impressions, CTR, Position. No data: stop and
   report "no new Search Console data" in one line. Never invent queries.
3. Run `python tools/seo/gaps.py`. If it prints "No gaps", stop and report that in one line.
4. Take the top gap whose query is a real question an Android user would ask about photos. Skip brand typos,
   adult or unrelated queries, and anything PixOrg cannot honestly answer (video search, cloud sync, iPhone).
   If the nearest guide covers 30 to 60 % of it, improve that guide (add the missing section, widen its
   `keywords:`) instead of writing a new one.
5. Write the guide to `_guides/<slug>.md` exactly as `STYLE.md` says: honest general method first, then
   "In PixOrg" only with features listed in STYLE.md, 500 to 900 words, `query:` set to the gap's query,
   `related:` naming 1 to 3 existing slugs. Add a one-line link to the new guide inside the two most related
   existing guides (a sentence in the body, not only `related:`), so the new page is linked from pages that
   already get impressions.
6. Check it: `python tools/seo/gaps.py --check "<query>"` says covered; the front matter parses; every PixOrg
   claim is in STYLE.md's feature list; no em-dashes, no exclamation marks, no emoji.
7. Commit on a branch `guide/<slug>`, push, open a pull request titled `Guide: <title>` whose body has the
   gap's numbers (impressions, clicks, position), the two pages you linked from, and the one thing you were
   unsure about, if any. One PR per week at most. Stop.

## Never

- Publish without a pull request, or merge your own PR.
- Write more than one new guide per run. A gap you skipped waits for next week.
- Claim a feature, number or comparison that is not in STYLE.md or the PicOrg repo.
- Touch `app-ads.txt`, `_config.yml`, the layouts, or the privacy repo.
- Add screenshots of anyone's real photos. Only `assets/shots/*` (public demo photos).
