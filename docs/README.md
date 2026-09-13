# He Lab — AI for Biology and Human Intelligence

Static website for He Lab. The site uses plain HTML, CSS, JavaScript, and local image assets.

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

Commit the generator and regenerated HTML together. The selected logo uses mist violet (`#8A7CA5`) and indigo (`#44496B`). Its exported assets are in `images/`.

## GitHub Pages

In repository **Settings → Pages**, select **Deploy from a branch**, choose **main**, and select **/docs**. The `.nojekyll` file serves these static files directly.

The public website is https://yichun-he-lab.github.io/, served from the `yichun-he-lab/yichun-he-lab.github.io` repository. Fonts are hosted locally, with their licenses in `fonts/`.
