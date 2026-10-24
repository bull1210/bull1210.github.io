---
title: How to search the text inside your photos on Android
description: Find the screenshot, receipt, sign or whiteboard by a word that is written on it, and copy the text out, without uploading anything.
date: 2026-10-25
query: search text in photos android
slug: find-text-in-photos
keywords: ocr photos find words in screenshots copy text from photo search receipts signs whiteboard
related: [search-photos-by-description, find-receipts-in-photos, declutter-phone-photos]
image: /assets/pins/find-text-in-photos.jpg
---

A lot of what sits in a phone's gallery is not really a photo. It is a screenshot of a booking, a shot of
the Wi-Fi password on the back of the router, a receipt, a whiteboard from a meeting, a shop sign you meant
to look up later. You know a word that is on it. You do not know when you took it.

Reading the words in pictures is called OCR, and phones are good at it now. The question is which app does
it, and where.

## What already reads text in photos

- **Google Photos** reads the text in photos it has backed up and lets you search for it. Open a photo and
  tap Lens to select and copy the words. It works well, but only for photos that have been uploaded, and the
  reading happens on Google's servers.
- **Google Lens** on its own reads any photo you open with it, one at a time. Good for copying a phone number
  off a sign; no use for finding which of 300 screenshots has "booking reference" on it.
- **The phone's gallery** sometimes offers text selection when you open a photo (Samsung and Pixel do). Few
  of them let you search by that text across the library.
- **Files** searches file names, and a screenshot is called Screenshot_20250302-184455.png.

If everything you own is in Google Photos, its search does this job. If some of your photos stay on the
phone, you need an app that reads them there.

## In PixOrg

PixOrg reads the words in every photo as part of indexing, on the phone, and puts them in the same search
box as everything else.

1. Open PixOrg and tap **Search**.
2. Type a word or two that is written on the picture: "booking reference", "electricity bill", "KA 03",
   "agenda". Exact words work best; a word of five letters or more also matches when you type its start.
3. Photos with those words come first. If you add a kind, PixOrg limits the list: "screenshots with
   password", "receipts from March 2025".
4. Open the photo. Long-press the text in it to select it, then copy. The Wi-Fi password goes straight to
   the clipboard; you do not type it off the picture.

![The AI tab in PixOrg](/assets/shots/05_ai.jpg)

Some of the text-heavy photos get their own pages, so you do not have to search at all:

- **Receipts** collects the bills and shop receipts it recognised, reads the totals and can export them as a
  spreadsheet. There is a [separate guide to receipts](/guides/find-receipts-in-photos/).
- **Whiteboards** collects the boards and flip charts.
- **Screenshots** lists screenshots on their own, newest first, and Declutter offers the old ones for
  deletion.

A photo that is mostly text, such as a screenshot or a scanned letter, is treated as a document rather than
a picture: when you search for "beach", it is not shown among the beach photos just because the word "beach"
appears in it somewhere. When you search for a word, it is.

## What it does not read

PixOrg reads text in the Latin alphabet, so English and most European languages. Tamil, Hindi and other
scripts are not read, and handwriting is hit and miss, as it is everywhere. Very small print on a receipt
photographed from far away is often missed; a closer photo is read better. A photo PixOrg has not reached yet
(the Settings page shows what is left) cannot be found by its words.

## Privacy

The text reader runs on the phone, and the words it reads are stored only in PixOrg's own database there.
That matters more for this kind of photo than for any other, because screenshots and receipts are where the
account numbers, addresses and passwords live. PixOrg has no account and no server. The free version shows
small ads under the grid; the ad network sees an advertising ID, never a photo or the text in it.
