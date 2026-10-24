---
title: PixOrg, the offline AI photo gallery for Android
description: Find any photo by describing it, sort one Camera folder into real folders, find every photo of a person, and keep it all on your phone. Guides and help for PixOrg.
permalink: /
---
# Find any photo. Just describe it.

<p class="lead">PixOrg is a photo gallery for Android with the AI on the phone. Type "sunset at the beach" or "electricity bill" and it finds the photo. It groups your days into Moments, finds every photo of a person, sorts the Camera folder into folders, and makes short movies with your own music. Nothing about a photo ever leaves your phone.</p>

{% include play-card.html %}

## Guides

How to do the everyday photo jobs on Android, with and without PixOrg.

<ul class="guides">
{% assign guides = site.guides | sort: "date" | reverse %}
{% for g in guides %}
  <li><a href="{{ g.url | relative_url }}">{{ g.title }}</a><p>{{ g.description }}</p></li>
{% endfor %}
</ul>

## Privacy

The search model, the text reader and the face models all run on the phone. PixOrg has no account and no server. The free version shows small Google ads, which see an advertising ID and never a photo. The full [privacy policy]({{ site.privacy_url }}) says exactly what the ad SDK sees.
