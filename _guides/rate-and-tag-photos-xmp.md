---
title: How to rate and tag photos on Android and keep the ratings
description: Star ratings and tags that live inside the photo file, so Lightroom, Windows and your next gallery app read them, plus albums that fill themselves.
date: 2026-10-25
query: rate photos android keep ratings
slug: rate-and-tag-photos-xmp
keywords: star rating photos tags xmp metadata smart album favourites portable lightroom windows explorer
related: [backup-photo-app-settings, photo-gallery-without-cloud, declutter-phone-photos]
image: /assets/pins/rate-and-tag-photos-xmp.jpg
---

You go through a trip's photos and mark the good ones. A year later you change phone, or gallery app, or
you copy everything to a PC, and the marks are gone. The favourites were a list inside one app, and the app
is not there any more.

There has been a standard way to store a rating in the photo itself for twenty years. Few phone apps use it.

## Where ratings usually go

- **Google Photos favourites** are kept in your Google account. Another app on the same phone cannot see them,
  and a photo copied out of Google Photos carries no sign of having been a favourite.
- **The phone's gallery** (Samsung, Xiaomi) keeps favourites in its own database. They vanish with a factory
  reset or a different brand of phone.
- **Lightroom, Windows Explorer, macOS Finder, digiKam** read and write the rating inside the file, in a block
  called XMP: `xmp:Rating` from 1 to 5 and `dc:subject` for tags. A photo rated 4 in Lightroom shows four
  stars in Windows and in any app that reads XMP. This is the portable way.

If you only ever use one app on one phone, where the rating lives does not matter. If you expect the photos
to outlive the app, it does.

## In PixOrg

PixOrg writes ratings and tags into the photo, the same way desktop tools do, so they travel with the file.

1. Open a photo. Tap the stars under it to rate it 1 to 5, or tap **Tag** and type a word: "portfolio",
   "print", "kids".
2. To rate or tag several at once, long-press in any grid, tick the photos, then **Rate** or **Tag** in the
   bar at the bottom.
3. The first time, Android asks you to allow PixOrg to modify the files. Allow it once for the selection.
   The rating is then written into the JPEG itself; for a PNG, HEIC or RAW file, it goes into a small `.xmp`
   file next to it, which is what Lightroom does too.
4. Copy the photo to a PC and the stars appear in Windows Explorer's details and in Lightroom's filter. Open it
   in another gallery that reads XMP and the rating is there.

Ratings already in your files are read when PixOrg scans them, so a library rated on a PC arrives rated.

![Albums in PixOrg](/assets/shots/08_albums.jpg)

## Albums that fill themselves

Ratings and tags are more useful when something acts on them. PixOrg's smart albums are rules:

- "4 stars and up" collects the best of everything, forever, as you rate.
- "Tag: print, this year" is the list for the photo shop.
- "5 stars, in Camera, 2025" and similar: a rule can combine rating, tags, folder, dates and kind.

Make one from **Albums**, tap **New smart album**, and set the rules. The album updates itself as you rate
and tag; nothing is copied or moved.

Rated and favourite photos are also protected: Declutter never suggests deleting a photo you have rated, and
when it finds duplicates the rated copy is the one it proposes to keep.

## What to know

Writing into a file changes its modified date, which some backup tools treat as a new file; the first big
rating session can make a backup run longer. The photo itself is not re-encoded, so there is no loss of
quality. XMP is a widely read standard but not a universal one: Google Photos ignores ratings in files, and
a few galleries show tags but not stars. A rating you want to keep is still safer in the file than in any
app's database, including PixOrg's.

## Privacy

A rating or a tag is written into your own file on your own phone, and nowhere else. PixOrg has no account
and no server, so your tags are not a profile of you anywhere. The free version shows small ads under the
grid; the ad network sees an advertising ID, never a photo, a rating or a tag.
