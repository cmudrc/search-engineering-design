---
title: Publications
layout: splash
permalink: /publications/

header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/publications.jpg
excerpt: ""

---
<ol>
  <!-- Print the accepted manuscripts -->
  {% for pub in site.posts %}
    {% if pub[include.variable] == include.value %}
      <li>
        {% if pub.style %}<u>{{ pub.style }}:</u>{% endif %}
        {% include author_list.html object=pub bold=false %}
        ({{ pub.year }}).
        <a href="{{ pub.url | relative_url  }}">"{{ pub.title }}."</a>
        <i>{{ pub.venue }}</i>{% if pub.volume %}, vol. {{ pub.volume }}{% endif %}{% if pub.issue %}({{ pub.issue }}){% endif %}{% if pub.pages %}, pp. {{ pub.pages }}{% endif %}.
      </li>
    {% endif %}
  {% endfor %}
</ol>
