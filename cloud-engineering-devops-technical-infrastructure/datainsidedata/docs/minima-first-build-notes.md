# title: "Jekyll Build Notes: Layers 1–4"

## A workshop-ready, layered guide to how DataInsideData.com was built and hardened on Minima—future-proofed for Minimal Mistakes."

## Introduction

**Layers 1–4: Core mechanics → structure → navigation → production hardening**  
_DataInsideData.com build notes (project-ready, workshop-friendly)_

> **Intent:** This document captures the **exact, repeatable process** used to build DataInsideData.com on **Minima**, with **safe overrides** and **production hygiene**, while staying **teachable** and **migration-friendly** for a future move to **Minimal Mistakes**.

---

### Executive summary (what you get by following this)

## What’s included

- Layers 1–4 breakdown (mechanics → structure → navigation → production)
- Safe override strategy (Minima-first)
- SEO + sitemap + feed + robots hygiene
- URL stability strategy (renames + redirects)
- Private repo → public repo deploy model (CI/CD)

**By the end of Layer 4 you'll have**:

- A clean **local dev loop** that matches production styling
- Clear **information architecture** (header nav + footer utilities)
- Safe, minimal **theme overrides** (footer/head + custom CSS)
- **SEO + discovery endpoints**: `/sitemap.xml`, `/feed.xml`, `/robots.txt`
- **Pagination** that scales (and won’t surprise you later)
- A **branch/PR workflow** that integrates with your private→public deploy pipeline (If you chose to go in that direction.)

---

## Layer 1 — Core Jekyll mechanics

### What Jekyll is

Jekyll is a **static site generator**. It compiles content into **static assets**:

- HTML
- CSS
- JavaScript
- XML (feed/sitemap)

There is no runtime database or request-time backend. Hosting becomes simple: serve static files.

### The local build loop

```bash
bundle install           # only when Gemfile changes
bundle exec jekyll serve # execute build
```

What `jekyll serve` does:

- Builds the site into `_site/`
- Starts a local server (typically `http://localhost:4000`)
- Watches for file changes and rebuilds automatically

**Important:** changing `_config.yml` requires a restart. That’s expected.

### Front matter (why it exists)

Front matter connects **content** to **structure**. Without it, Jekyll may treat a file as a raw asset and skip layout/Liquid processing.

Example listing page:

```yml
---
layout: home
title: Posts
permalink: /blog/
---
```

---

## Layer 2 — Structure, layouts, defaults, and “theme resolution”

### Rendering hierarchy (critical concept)

Jekyll resolves files in this order:

1. **Your repo** (site source)
2. **Theme gem** (Minima)
3. **Fallback behavior**

If you create a file in your repo with the **same path + filename** as a theme file, **your version wins** automatically.

### Why `_includes`, `_layouts`, `_sass` may be “missing”

When using a gem theme, those directories live inside the theme gem. You only create them when you need an override.

This keeps your repo:

- smaller
- cleaner
- upgrade-safe

### Defaults in `_config.yml` (remove repetition)

Use defaults to prevent repeated front matter across many files:

```yml
defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: post

  - scope:
      path: ""
      type: pages
    values:
      layout: page
```

**Benefit:** less copy/paste, fewer mistakes, easier scaling.

---

## Layer 3 — Pages, home vs blog, navigation

### One canonical homepage

Your homepage is defined by `index.md` / `index.markdown` at `/`.

Example:

```yml
---
layout: home
title: ""
permalink: /
---
```

Rule:
> One homepage. Avoid creating multiple pages that compete for `/`.

## Blog index page

Create a dedicated post listing page at `/blog/`:

```yml
---
layout: home
title: Posts
list_title: Recent & relevant
permalink: /blog/
---
```

## Navigation control (Minima)

Header navigation is controlled explicitly with `header_pages`:

```yml
header_pages:
  - start-here.markdown
  - blog.markdown
  - projects/projects.markdown
  - about.markdown
  - contact/contact.markdown
```

Notes:

- In Minima, the site title links to `/` (so a separate “Home” item is optional).
- Keep the header lean and move “utility links” into the footer.

## First safe override: footer

First override introduced:

```bash
_includes/footer.html
```

Why footer is a safe first override:

- low coupling
- easy to test visually
- minimal risk during upgrades

Rule of thumb:
> Override edges (footer/meta) before the spine (header/layouts).

---

## Layer 4 — Business + production hardening (Minima → future‑proof)

### 4.0 Goals

Layer 4 makes the site:

- business-friendly (clear nav + legal links)
- production-friendly (SEO, sitemap, robots)
- maintainable (minimal overrides)
- upgrade-friendly (future Minimal Mistakes)

## 4.1 Information architecture

### Header nav (primary actions)

Keep header nav lean:

- Posts
- Projects
- About
- Contact

### Footer (utility + legal)

Move these to footer:

- Archive
- Sitemap
- RSS
- Privacy Policy
- Terms of Use

Why:

- archive/sitemap/RSS are secondary
- legal links belong in the footer on most professional sites

## 4.2 Plugins (SEO + discovery)

Enable:

```yml
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap
```

What they do:

- `jekyll-feed` → `/feed.xml`
- `jekyll-seo-tag` → consistent SEO/meta via `% seo %`
- `jekyll-sitemap` → `/sitemap.xml`

## 4.3 Excerpts + listing pages

Show excerpts on listing pages:

```yml
minima:
  show_excerpts: true
```

Then add per-post front matter excerpts:

```yml
excerpt: "One sentence that sells the post."
```

Rule of thumb (DID style):

- 1 sentence
- clear value
- ~120–180 characters

## 4.4 Pagination (scales when content grows)

Config:

```yml
paginate: 5
paginate_path: "/blog/page:num/"
```

Pagination typically requires `jekyll-paginate`.

`Gemfile`

```ruby
gem "jekyll-paginate"
```

`_config.ym`

```yml
plugins:
  - jekyll-paginate
```

## 4.5 Safe head + custom CSS strategy

Override:

```bash
_includes/head.html
```

and load custom CSS after Minima’s main.css:

```html
<link rel="stylesheet" href="{{ "/assets/main.css" | relative_url }}">
<link rel="stylesheet" href="{{ "/assets/css/custom.css" | relative_url }}">
```

Custom CSS file:

```css
assets/css/custom.css
```

Principle:
> Don’t fork the theme. Layer over it.

## 4.6 robots.txt + verifications

Add `robots.txt` at repo root:

```markdown
User-agent: *
Allow: /

Sitemap: https://datainsidedata.com/sitemap.xml
```

Verify locally:

- `/sitemap.xml`
- `/feed.xml`
- `/robots.txt`

## 4.7 URL stability: renames + redirects

If you rename a post after it’s been generated or shared, use `redirect_from`:

```yml
redirect_from:
  - /blog/2026/01/11/old-slug.html
  - /2026/01/11/old-slug.html
```

Optional: add `jekyll-redirect-from` for safer refactors:

```yml
plugins:
  - jekyll-redirect-from
```

## 4.8 Standardize permalinks (recommended next)

To make all post URLs consistently live under `/blog/`, add:

```yml
permalink: /blog/:year/:month/:day/:title:output_ext
```

This reduces accidental 404s and keeps URLs predictable.

---

## Dual Repo Plan: Branch/PR Workflow with Deploy Confidence

> In some upcoming posts, I’ll be adding guides on creating Git branches, opening and merging PRs, and setting up GitHub Actions workflows. I’ll link them here as they go live.

### What you’re protecting

- Private repo: **source of truth** (Jekyll source)
- Public repo: **compiled output** only
- GitHub Actions builds private → pushes into public → Pages serves from `gh-pages`

### Safe PR workflow

Example:

1. Create a branch: `feat/*` or `chore/*`
2. Commit small, logical changes
3. Open PR (describe what/why + local test notes)
4. Merge to main
5. CI builds + deploys automatically

### Pre-merge checklist

Run the following command:

```bash
bundle exec jekyll clean && bundle exec jekyll serve
```

Then verify if the following renders in the browser (``http://localhost:4000``):

- `/` home
- `/blog/` and `/blog/page2/` (if applicable)
- `/archive/`
- `/sitemap.xml`, `/feed.xml`, `/robots.txt` 

---

**Data Inside Data™**  
Tech Hands, a Science Mind, and a Heart for Community™
