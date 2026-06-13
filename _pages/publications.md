---
layout: page
permalink: /pubs/
title: PUBLICATIONS
description: In reverse chronological order; entries marked Preprint are under submission.
years: [2026, 2025, 2024, 2023, 2022, 2021, 2019]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

<p>See also my <a href="https://scholar.google.com/citations?user=9DVUpAEAAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar</a> profile.</p>

<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
