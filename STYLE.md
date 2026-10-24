# How a PixOrg guide is written

Every guide in `_guides/` follows this. The weekly routine and anyone writing by hand read it first.

## One guide, one question

A guide answers one search query a real Android user types, in the words they would type it. The query
is the `query:` field in the front matter and the title answers it. One guide per question; if the
question is already covered (`python tools/seo/gaps.py --check "<query>"` says so), improve that guide
instead of writing a second one.

## Honest first, PixOrg second

The reader came for the job, not for us. So:

1. Open with the job in two or three plain sentences: what the reader wants and why it is awkward on Android.
2. Give the general way first when one exists (Google Photos, Files, the phone's own gallery, a camera setting).
3. Then "In PixOrg": exact taps, as the app really is. Never a feature PixOrg does not have, never a number
   we have not measured. If unsure what the app does, look at `docs/` and `lib/l10n/app_en.arb` in the PicOrg
   repo, or leave it out.
4. Close with one paragraph on privacy where it matters (the models run on the phone; nothing about a
   photo leaves it) and let the Play card (added by the layout) do the asking. No second call to action.

## Voice

Plain English, short sentences, "you". No marketing words (seamless, powerful, effortless, revolutionary),
no exclamation marks, no emoji, no em-dashes. Say "photo", not "image" or "asset". Say what a thing does,
not that it is smart. 500 to 900 words. Headings are H2 (`##`) and are questions or plain nouns, never
"Introduction" or "Conclusion". A numbered list for taps, a bulleted list for choices.

## What PixOrg actually does (checked 2026-10-25)

- Search: type a description ("birthday cake with candles") or the words inside a photo (receipts, signs,
  screenshots). English only. Searches names once a person is named ("Amma in 2024"). Dates, colours and
  kinds work ("receipts from March 2025", "red car", "screenshots"). Folder scope with a cue ("in Camera").
  The first results come while the library is still being read ("Searched N of M photos").
- Moments: days, trips and festivals grouped by time and place, named from what is in them ("Diwali",
  "Day out in Mysuru", "With Amma"). Renaming a moment sticks. Folders the user made become moments too.
- People: faces grouped on the phone. Name once; the name is searchable. Paintings, idols, statues and
  screenshots are left out. Small or blurred faces are stored but not grouped. A person can be hidden,
  merged ("Same as…") or split ("Not <name>").
- Move to folder: a moment or a selection moved into a new or existing folder under DCIM or Pictures,
  without the original being deleted before the copy is verified. Rename folder, copy, resize.
- Declutter: forwards, old screenshots, duplicates, similar shots (bursts), blurry or dark shots, old chat
  media, big videos. Everything is unticked except exact duplicates; the user reviews and deletes. Deleted
  photos go to Android's Bin on Android 11+ (30 days). Duplicates is Declutter's second tab. Rated or
  favourite photos and photos of a named person are never suggested.
- Receipts: found automatically, totals read, CSV export. Whiteboards and screenshots have their own pages.
  Live Text: the words in a photo can be selected and copied.
- Ratings and tags: written into the photo (XMP), so another app or a PC reads them. Smart albums with rules.
- Vault: encrypted files in a folder the user picks (survives uninstall), unlocked with the phone's screen
  lock and recoverable with a passphrase alone (`tool/decrypt_vault.py` in the repo decrypts a file with the
  key file and passphrase, no app needed). Videos are not vaulted.
- Backup: one `.pixbak` file with ratings, tags, people, moments, settings and the vault's key. Photos are
  not in it. Restore on a new install.
- Movies: pick photos or a moment, choose order and a song from the phone (and where it starts), 1080p
  portrait, saved to Movies/PixOrg. Free. Collage (photos never cropped), PDF, resize.
- Around this: from any photo, the moment or the day it belongs to.
- Visual Look Up: what a photo shows, from the same model.
- Indexing: runs on the phone, newest photos first, one year at a time on big libraries; it asks before
  reading older years. It pauses during calls and keeps going in the background when allowed.
- Ads: small bars under grids and an occasional full-screen ad after a finished task from the second day.
  Every feature is free. PixOrg Pro removes ads (monthly, yearly or one payment).
- Not in PixOrg: cloud backup, sync, editing beyond crop/rotate (it hands off to the phone's editor),
  video search, Tamil/Hindi search, a desktop app, an iPhone version.

## Front matter

```yaml
---
title: How to find a photo by describing it on Android   # answers the query, 45-65 chars
description: One sentence, 120-160 chars, what the reader will be able to do.
date: 2026-10-25
query: search photos by description android              # the search the guide targets
slug: search-photos-by-description                       # file name without .md, used by related:
keywords: describe photo search natural language gallery # other words the guide answers (for gaps.py)
related: [find-text-in-photos, find-photos-of-a-person]  # 1-3 slugs of other guides
image: /assets/shots/01_search.jpg                       # optional; one of assets/shots/*
---
```

Screenshots in `assets/shots/` are from the public demo library (Wikimedia Commons photos), never from
anyone's own phone. Use them as `![PixOrg's search results for "beach"](/assets/shots/01_search.jpg)`.
Never add new screenshots that show real people's photos.
