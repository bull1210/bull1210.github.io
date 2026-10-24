---
title: How to hide photos on Android securely
description: Put private photos behind your screen lock in an encrypted vault you can still open if the app is gone or the phone is lost, with a passphrase alone.
date: 2026-10-25
query: hide photos on android securely
slug: hide-photos-vault
keywords: private photos locked folder encrypted vault hidden album secure gallery recover
related: [backup-photo-app-settings, photo-gallery-without-cloud, find-photos-of-a-person]
---

Some photos should not be in the grid when you hand your phone to a child to see the holiday pictures:
a scan of your passport, a medical report, a photo meant for one person. Hiding them is easy. Hiding them
in a way that survives a lost phone, a reinstalled app or a forgotten app password is where most answers
fall down.

The useful test for any hiding method is: if this phone died tonight, could I get the photos back, and
could anyone else?

## What Android already offers

- **Google Photos Locked Folder** moves photos behind your screen lock. It is simple and built in. On
  older versions the folder lived only on that phone and was not backed up; newer versions can back it up
  to your Google account. Either way the photos are tied to Google Photos, and if you lose access to the
  account you lose the folder.
- **Samsung Secure Folder** is a separate encrypted space on Samsung phones, with its own gallery. Strong,
  but it exists on Samsung phones only and does not move to another brand.
- **A ".nomedia" file** in a folder hides that folder from galleries. It is not security: a file manager
  shows everything, and so does the next gallery app you install.
- **Vault apps from the store** often encrypt with their own password. If you forget it, or the app is
  removed from the store, the photos are gone. Several have been caught uploading to their own servers.

## In PixOrg

PixOrg's Vault encrypts each photo into its own file, in a folder you choose, and opens with the phone's
own screen lock. There is also a passphrase, and the passphrase alone is enough to get the photos back,
with or without PixOrg.

1. Open PixOrg, tap **Albums**, then **Vault**.
2. The first time, pick a folder for the vault (anywhere on the phone or an SD card) and set a passphrase
   of at least eight characters, not all digits. Write it down somewhere safe; it is the recovery key.
3. Long-press photos anywhere in PixOrg and tap **Vault** in the action bar. They are encrypted into the
   vault folder and removed from the normal library, so no gallery app shows them.
4. Open the Vault with your fingerprint or screen-lock PIN. Photos open and share from there as usual.
   **Restore** moves one back to the library.

Videos cannot be vaulted; the Vault is for photos.

What makes it recoverable:

- Each vaulted photo is a self-contained encrypted file (AES-256). Next to them sits a key file protected by
  your passphrase. Those files plus the passphrase are the whole vault; PixOrg is just a convenient way to
  open them. The PixOrg repository includes a small script that decrypts a vault with the key file and
  passphrase on a PC, so the photos are never locked to an app that might disappear.
- The vault folder survives uninstalling PixOrg. Install it again, point it at the same folder, enter the
  passphrase, and the vault is back. Copy the folder to a PC or a drive and it is a backup.
- A PixOrg backup file includes the vault's key, so a restored backup opens the vault without retyping the
  passphrase; see [backing up PixOrg's own data](/guides/backup-photo-app-settings/).

If the phone has no screen lock, the Vault still works but shows an amber warning, because anyone holding
the phone can open the app. Set a screen lock first.

## What it does not do

The Vault hides photos from galleries and encrypts them on disk. It does not hide that PixOrg is on the
phone, and it does not stop someone who knows your screen-lock PIN. Android blacks out the opened vault in
screen recordings and screenshots; it cannot stop a camera pointed at the screen.

## Privacy

Encryption happens on the phone, with a key made from your passphrase, and nothing about a vaulted photo,
including the fact that it exists, is sent anywhere. PixOrg shows no ads in the Vault. A vaulted photo leaves search,
People, Moments and every other page of the library; only the Vault shows it.
