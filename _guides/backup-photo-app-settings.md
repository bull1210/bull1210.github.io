---
title: How to move your photo ratings, people and albums to a new phone
description: Save everything you taught your gallery app, names, ratings, tags, moments and the vault key, to one file, and bring it back on a new phone or after a reinstall.
date: 2026-10-25
query: backup photo organizer settings new phone
slug: backup-photo-app-settings
keywords: backup gallery app data restore new phone transfer people names ratings albums pixbak reinstall
related: [rate-and-tag-photos-xmp, hide-photos-vault, photo-gallery-without-cloud]
image: /assets/pins/backup-photo-app-settings.jpg
---

A gallery app learns things from you over a year. Which face is Amma. Which photos are five stars. That the
moment in June was "Goa, not Gokarna". Which forwards you have already reviewed. Then you buy a new phone, or
reinstall the app to fix something, and the photos come across but the year of teaching does not.

The photos and what you know about them are two different things, and they need two different backups.

## Backing up the photos

Nothing here replaces copying the files. On Android that is any of:

- **A cloud** you trust with them (Google Photos, OneDrive, a NAS app). Convenient, costs space, and the
  photos leave the phone.
- **A PC over USB.** Plug in, choose File transfer, copy `DCIM` and `Pictures`. Free, offline, and you have
  to remember to do it.
- **Phone-to-phone transfer** when you set up the new phone (Google's "Copy apps and data", Samsung Smart
  Switch, Xiaomi's Mi Mover). These copy the photos and most apps' data, but not reliably an app's own
  database, and not a folder the app was given by permission.

Whatever you use, the photo files are the same files; a gallery app that does not alter them, which PixOrg
does not, is indifferent to how they travel.

## Backing up what the app knows

Some of what you teach PixOrg is written into the photos themselves. Ratings and tags go into the file as XMP,
so they move with the photo and need no separate backup; a copied photo arrives rated. There is a
[guide to that](/guides/rate-and-tag-photos-xmp/).

The rest lives in PixOrg's database on the phone, and for that there is one file.

1. Open **Settings** (the gear on any tab), then **Backup**.
2. Tap **Back up now**, set a passphrase for the file, and pick where to save it. A file called
   `pixorg-backup-<date>.pixbak` is written. Save it to Drive, a PC or an SD card; anywhere you would keep a
   document. Keep the passphrase somewhere else; the file is useless without it.
3. The file holds: the names and groupings in People, your ratings and tags (again, so they are there even
   for photos you have not copied), renamed Moments, smart albums and their rules, your settings, the
   Declutter review log, and the key to your vault.
4. It does not hold the photos, and it does not hold the vault's encrypted files. Those are files, and they
   travel with the file backup above.

The file is encrypted, so a copy on Drive is not readable without PixOrg.

## Restoring on a new phone

1. Copy the photos to the new phone first, into the same folders if you can (`DCIM/Camera` to
   `DCIM/Camera`). Ratings and tags come with them.
2. Install PixOrg, open it, go to **Settings**, then **Backup**, then **Restore a backup**, pick the `.pixbak`
   file and enter its passphrase. PixOrg restarts with your people, names, moments and settings.
3. Let it read the library. Photos it recognises from the backup keep their people and moments; new ones are
   read as usual.

A backup from a newer version of PixOrg is refused by an older one, so update first and restore second.

## The vault survives on its own

The vault is a folder you chose, full of encrypted `.pixvault` files and a `vault.key`. It survives an
uninstall, because it is your folder, not the app's. On a new phone, copy that folder across with the rest,
open PixOrg's Vault, and point it at the folder; it rebuilds the list from the files. With the folder, the key
file and your passphrase you can even open the photos without PixOrg, which is the point of the design. See
[hiding photos in the vault](/guides/hide-photos-vault/).

## Privacy

The backup is a file on your phone, encrypted before it is written, and it goes only where you put it. PixOrg
has no account and no server, so there is no copy of your names and ratings anywhere you did not choose. The
free version shows small ads under the grid; the ad network sees an advertising ID, never a photo or a backup.
