# He Lab — AI for Biology and Human Intelligence

Current He Lab website, published from the repository’s `docs/` directory. The site uses plain HTML, CSS, JavaScript, and local image assets.

## Preview locally

```sh
python3 -m http.server 8001 --bind 127.0.0.1
```

Open http://127.0.0.1:8001/.

## Update content

Edit `build_site.py` for shared layout and page copy, `site-data.json` for publications, `lab.css` for styles, and `lab.js` for navigation. Then run:

```sh
python3 build_site.py
```

Run these commands from `docs/`. Commit the generator and regenerated HTML together. The selected logo uses mist violet (`#8A7CA5`) and indigo (`#44496B`). Its exported assets are in `images/`.

## GitHub Pages

In repository **Settings → Pages**, select **Deploy from a branch**, choose the default branch, and select **/docs**. The `.nojekyll` file serves these static files directly.

The website uses relative asset paths, so it supports either an account site or a project site. An account site at `https://yichunhelab.github.io/` requires both the GitHub account or organization name `yichunhelab` and repository name `yichunhelab.github.io`.
