# haosun.info

Personal homepage of [Hao Sun](https://haosun.info). Plain static HTML and CSS —
no build step, no framework.

```
index.html      home: about, news, research, publications, software, talks, awards, service
teaching.html   teaching and student supervision
css/style.css   the whole design; ETH Zurich palette, Inter + Source Serif 4
js/site.js      colour-theme toggle and nav section highlighting
assets/         portrait, paper PDFs, slides
```

To preview locally:

```sh
python3 -m http.server 8000   # then open http://localhost:8000
```

Pushing to `main` runs `.github/workflows/deploy.yml`, which copies the tree onto
the `gh-pages` branch that GitHub Pages serves. (If you switch the Pages source
to `main` in the repository settings, the workflow can be deleted.)
