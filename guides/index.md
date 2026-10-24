---
title: PixOrg guides
description: Short, honest guides to finding, sorting, cleaning up and protecting photos on Android.
permalink: /guides/
---
# Guides

<ul class="guides">
{% assign guides = site.guides | sort: "date" | reverse %}
{% for g in guides %}
  <li><a href="{{ g.url | relative_url }}">{{ g.title }}</a><p>{{ g.description }}</p></li>
{% endfor %}
</ul>
