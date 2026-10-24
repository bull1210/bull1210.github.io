---
title: How to move photos out of the Camera folder into folders on Android
description: Turn one Camera pile of thousands of photos into folders by trip and occasion, without losing a single original along the way.
date: 2026-10-25
query: move photos from camera folder to another folder android
slug: sort-camera-folder-into-folders
keywords: organize camera roll folders dcim sort photos into albums move trip photos new folder
related: [declutter-phone-photos, memory-video-from-photos, find-duplicate-photos]
image: /assets/shots/02_folders.jpg
---

Every photo you take lands in the same place: a folder called Camera, inside DCIM. After a few years it
holds eleven thousand photos in one long scroll, and the trip to Hampi sits somewhere between a parking
ticket and a screenshot of a recipe. Albums in a gallery app can tidy the view, but they are a label in
that one app. The folder is what every app, your PC and your next phone will see.

So the job is real: get the trip out of Camera and into a folder called Hampi 2024, and do it for the other
trips too, without spending a weekend on it.

## Moving photos with the Files app

Android's own Files app (or Samsung's My Files) can move files between folders.

1. Open Files and go to Internal storage, then DCIM, then Camera.
2. Long-press a photo, then tap the others you want. The list shows file names and tiny thumbnails, so
   picking the right eighty photos out of eleven thousand is slow.
3. Tap the menu, then **Move to**, and pick or create a folder.

It works, and nothing extra is installed. The trouble is step 2. File managers sort by name or date and
show one or two photos per row, so you cannot see a trip as a trip. People usually move one album and give
up.

Gallery apps are the other way round: they show the photos well but mostly make albums, not folders. Google
Photos has no "move to folder" at all for photos on the phone. Some phone galleries (Samsung, Xiaomi) can
move to an album that is also a folder; check whether the result shows up in Files before relying on it.

## In PixOrg

PixOrg groups your photos into Moments by time and place, and a moment can be moved into a folder in one
go, so the trip is already selected for you.

1. Open PixOrg and tap **Moments**. Find the trip or the day, for example "Day out in Hampi" or "Diwali".
2. Open the moment and tap **Move**. Choose **Move all N photos** to take the whole moment, or long-press
   photos first and choose **Move N selected**.
3. Pick a folder, or tap **New folder** and type a name. New folders go under DCIM or Pictures, where every
   gallery and PC looks.
4. Android asks once for permission to modify the photos. Allow it. The move runs in the background and
   PixOrg shows a progress card; you can keep using the app.

![A folder made from a moment in PixOrg](/assets/shots/02_folders.jpg)

What happens behind the move:

- On Android 11 and later the photo is renamed into the new folder, which takes a moment per photo and
  copies nothing. On older phones PixOrg copies the file, checks the copy, and only then deletes the
  original. An original is never deleted before a verified copy exists.
- If the phone restarts or the app is closed halfway, a card offers to finish the move when you come back.
- The folder you made stays one moment in PixOrg, even if the photos span weeks, so "Hampi 2024" reads as a
  trip and not as four separate days.
- The folder is a real folder. Open Files, or plug the phone into a PC, and it is there with the photos in
  it. Delete PixOrg tomorrow and nothing is lost.

You can also rename a folder from Albums (**Rename folder**), and copy photos to a second folder instead
of moving them (**Copy**). PixOrg will not rename the Camera folder itself or other folders Android depends
on, so the camera app keeps working.

## A way to work through a big Camera folder

Do not try to sort eleven thousand photos in one sitting. Open Moments, scroll to a trip you recognise,
move it, and stop. Next week do another. Each move takes about a minute of your attention, and after a
few weekends the Camera folder holds only the everyday photos nobody needs to file.

Two things make the pile smaller before you start. Run [Declutter](/guides/declutter-phone-photos/) to
clear forwards, old screenshots and duplicates, and use the
[Duplicates tab](/guides/find-duplicate-photos/) so you do not move the same photo into two folders.

## Privacy

Sorting photos needs no network, and PixOrg has none. The moments that make a trip easy to pick are
worked out on the phone from the time, the place in the photo's own data and what the photos show. The
folder move is an ordinary file operation; no copy of a photo is made anywhere but on your phone.
