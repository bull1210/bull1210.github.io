---
title: Why your Xiaomi or Redmi photos have no location, and how to fix it
description: Xiaomi cameras do not save where a photo was taken unless you switch it on. Here is the setting, what it changes, and what no app can recover.
date: 2026-10-25
query: xiaomi photos no location
slug: xiaomi-photos-no-location
keywords: redmi camera gps photo location missing map empty geotag exif save location info hyperos miui
related: [search-photos-by-description, photo-gallery-without-cloud]
image: /assets/pins/xiaomi-photos-no-location.jpg
---

You open a map of your photos and it is empty, or you look at a photo's details and there is a date, a
camera, an aperture, and no place. On a Xiaomi, Redmi or POCO phone this is the normal state, not a fault.
The camera app does not save the location unless you ask it to.

## Why the location is missing

A photo's location is a pair of coordinates written into the file by the camera app, in the EXIF block next
to the date and the camera model. Most Android cameras write it as soon as you grant them the location
permission. Xiaomi's camera has its own switch, off by default in MIUI and HyperOS, and asks for nothing
until you find it.

Photos taken while that switch was off have no coordinates. There is nothing hidden to unlock: the number
was never written.

## Turn it on for new photos

1. Open the **Camera** app.
2. Tap the three lines (or the gear) at the top right, then **Settings**.
3. Find **Save location info** (some versions say "Location tags" or "Geotag") and switch it on.
4. The first time, Android asks for the location permission for Camera. Allow it "while using the app".

From the next photo on, the place is in the file. You can check in the Gallery app: open a photo, swipe up
or tap the info button, and the address appears under the date.

Two things to know:

- **Location needs GPS or a network.** Indoors and in the first seconds after opening the camera, the phone
  may not have a fix yet, and a photo taken then can still be without a place.
- **Sharing.** Xiaomi's share sheet has **Remove location info** on by default for some channels, and WhatsApp
  and most chat apps strip it anyway. Your own copy keeps the location; the one you send usually does not,
  which is the right way round.

## Old photos cannot be fixed by an app

No gallery, cloud or AI can know where a photo without coordinates was taken. Google Photos sometimes shows an
"estimated location" on a photo, which comes from your phone's Location History at that time, if you had it
on. A few desktop tools let you drag photos onto a map yourself. That is the whole menu.

What a gallery can do is make the location matter less, by grouping photos by time instead.

## In PixOrg

PixOrg groups photos into Moments by when they were taken and, when there are coordinates, by where. A
Xiaomi library without coordinates still gets its moments:

- Days out, trips and festivals are found from the times and gaps between photos, and named from what is in
  them ("Diwali", "Birthday", "With Amma") or by the date.
- Once **Save location info** is on, new moments also get their place: "Day out in Mysuru" rather than
  "Saturday 14 June". A trip is recognised as a trip when the photos are far from home.
- The **Map** page shows only photos that have coordinates. For a Xiaomi library that has just switched the
  setting on, it starts nearly empty and fills from that day forward. That is the camera, not the app, and
  it is the same in every gallery.

Search does not need a place either. "Beach in 2024", "temple", "receipts from March" work from the photo
and the date.

## Privacy

Location in a photo is a trade. It is what lets any gallery say "Mysuru" and what lets anyone you send the
original to see where you were. Keep the Camera switch on and let the share sheet strip it on the way out,
and you get both. In PixOrg the coordinates are read from the file on the phone and stay in its database
there; PixOrg has no server to send them to. The free version shows small ads under the grid; the ad network
sees an advertising ID, never a photo or its location.
