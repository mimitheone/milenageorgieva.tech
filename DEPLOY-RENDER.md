# Deploy on Render (private GitHub repo)

GitHub Pages on a **free personal** account usually does **not** publish a public site from a **private** repository. Hosting on **Render** avoids that limitation.

This repo ships:

- `render.yaml` — Blueprint for a **Docker-based web service** that builds the site and serves it with **nginx**
- `Dockerfile` — installs Cairo/Pango (needed for **social cards** / `cairosvg`), runs `mkdocs build`, copies `./site` into nginx

Native **Render Static Sites** cannot run `apt-get` during the build; MkDocs needs those system libraries, so Docker is used.

## One-time setup

1. Sign in at [Render](https://render.com/) and connect **GitHub**.
2. **New** → **Blueprint** (or **New** → **Web Service** with **Docker**).
3. Select the private repo and the `main` branch.
4. Render should detect `render.yaml`; confirm the Dockerfile path is `./Dockerfile`.
5. Deploy. When the build succeeds, open the `onrender.com` URL and check the site.

## Custom domain (`milenageorgieva.tech`)

1. Service → **Settings** → **Custom domains** → add your domain.
2. In DNS (e.g. Cloudflare), add the **CNAME** (or records) Render shows.
3. If the domain still pointed at **GitHub Pages**, update or remove those records so traffic goes to **Render**.

## GitHub Actions

`.github/workflows/ci.yml` only runs `mkdocs build` (validation). It does **not** deploy to GitHub Pages.
