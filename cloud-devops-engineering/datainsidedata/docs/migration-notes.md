---
noteId: "6deb85d022db11f194fd9f5d564fbc14"
tags:
  - "jekyll"
  - "minima"
  - "minimal-mistakes"
  - "migration"
  - "devops"
title: "Migrating from Minima to Minimal Mistakes (MM) — A Clean Approach"
date: "2026-01-26 12:00:00 -0500"
categories:
  - "jekyll"
  - "minimal-mistakes"
excerpt: "A step-by-step migration guide from Minima to Minimal Mistakes, including config, overrides, navigation, projects collections, and footer fixes."
toc: true
toc_sticky: true

---

## 1. Introduction

> This doc captures the build process, why I decided to migrate to MM, and the exact **clean migration + override** pattern I'm currently using.

When I started **DataInsideData.com**, I intentionally chose the Minima theme. Why? It was simple, clean, and perfect for learning how Jekyll works.

Since I was building to scale, I had to be prepared for when the site matured, so I needed:

- Stronger navigation
- Collections support
- Built‑in search
- Table of contents (TOC)
- Related posts
- A more flexible layout system

The decision was clear: migrate to **Minimal Mistakes** — and do it
cleanly.

This post documents the exact migration pattern I used.

## 2. Why Minimal Mistakes

Minimal Mistakes is more than a theme — it's a structured blogging
framework.

### Built-in Features

- Greedy Nav responsive menu
- Search (Lunr)
- TOC support
- Author profiles
- Related posts
- Breadcrumbs
- Collections support
- Archive layouts
- Skins

## Non–Built-In Search Options (Supported via Overrides or Integrations)

Lunr is great for relatively large sites, but there are non-built-in options that you may need to consider when your site gets **very** large:

- **Algolia DocSearch**
  - Requires the `jekyll-algolia` plugin
  - Needs API keys and indexing
  - Extremely fast and scalable for large sites

- **Simple-Jekyll-Search**
  - Lightweight, client-side JavaScript search
  - Uses a JSON index similar to Lunr
  - Easy drop-in replacement via `search.html` override

- **Pagefind**
  - Modern, Rust-based static search indexer
  - Very fast and works on GitHub Pages
  - Requires a build step (e.g., GitHub Actions)

- **Elasticlunr.js**
  - Lunr-compatible but more flexible
  - Pure client-side, no backend required
  - Integrated by swapping out the Lunr JS include

- **Meilisearch**
  - Requires hosting a backend search server
  - Fast, typo-tolerant, great for large datasets
  - Integrated via custom API calls in overridden layouts

- **Typesense**
  - Backend search engine with instant-search performance
  - Requires custom JS + layout overrides
  - Good for structured, large-scale content

- **Custom Search APIs**
  - Any REST API you build or host
  - Integrated by overriding `search.html` and adding custom JS
  - Useful for advanced or domain-specific search needs

### MM Tradeoffs

More power = more structure.

You must respect components like

- Its class system (`.masthead`, `.page__footer`, `.archive__item`, etc.)
- Its include pipeline
- Its SCSS hierarchy

---

## 3. Clean Migration Strategy (Avoiding Collisions)

If you previously customized [Minima](https://datainsidedata.com/projects/jekyll-from-zero-to-production/)

Jekyll will prefer your local `_includes/*` over theme includes.

That causes silent breakage.

### Step 1 — Disable Minima Overrides

Rename old overrides

```jekyll
_includes/header.html → header.minima.bak
_includes/head.html → head.minima.bak
_includes/footer.html → footer.minima.bak
```

Let MM load clean defaults first. Then override intentionally.

- After things work and you're comfortable, remove these files or place in a backup folder.

## 4. Correct `_config.yml` Setup

MM setup

``` yaml
# Use the MM theme instead of Minima
theme: minimal-mistakes-jekyll

# Select one of MM’s built-in skins
minimal_mistakes_skin: "default"

# Core plugins used by MM and this site
plugins:
  - jekyll-feed              # Generates RSS feed
  - jekyll-seo-tag           # Adds SEO meta tags
  - jekyll-sitemap           # Generates sitemap.xml
  - jekyll-paginate          # Enables pagination for blog index
  - jekyll-redirect-from     # Allows redirect_from in front matter
```

### Defaults Block

``` yaml
defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: false
      read_time: true
      related: true

  - scope:
      path: ""
      type: pages
    values:
      layout: single
      author_profile: false
```

### Collections (My Projects Collection)

``` yaml
# Custom collections allow structured content beyond blog posts
collections:
  projects:
    output: true                    # Required to generate HTML pages
    permalink: /projects/:name/     # Clean URLs without date structure
```

- output: true is critical — without it, Jekyll will not generate pages for this collection.

**Works with**

```bash
_projects/
```

and

```bash
projects/projects.markdown
```

---

## 5. Navigation (MM Native)

Navigation lives in

```yml
_data/navigation.yml
```

Example

``` yaml
main:
  - title: "Start Here"
    url: /
  - title: "Posts"
    url: /blog/
  - title: "Projects"
    url: /projects/
  - title: "About"
    url: /about/
  - title: "Contact"
    url: /contact/
```

### If your "Posts" link throw 404s

- Check permalink
- Check navigation.yml
- Ensure trailing slash consistency

## 6. SCSS Architecture (This is Critical)

Keep the ``main.scss`` file:

```bash
assets/css/main.scss
```

And the file must include the following so that MM can import necessary skins, styling, etc...

``` scss
---
---

// Required front matter so Jekyll processes this file
@charset "utf-8";

// Import selected MM skin
@import "minimal-mistakes/skins/{{ site.minimal_mistakes_skin | default: 'default' }}";

// Import full MM framework
@import "minimal-mistakes";

// Load your custom overrides last
@import "minimal-mistakes/custom";

```

- Order matters here. Custom overrides must load after the core framework to prevent specificity issues.

Put all styling overrides in:

```bash
_sass/minimal-mistakes/_custom.scss
```

Avoid maintaining separate Minima legacy `custom.css` files long-term.

- I renamed mine and moved to a backup folder in another directory.

---

## 7. Footer Override Strategy

Why Copy Instead of Rewriting?

- Jekyll prefers local overrides over theme files
- Partial rewrites can break layout structure
- Copying preserves upstream compatibility

Use the command below to locate the installed gem:

```bash
bundle show minimal-mistakes-jekyll
```

Then locate ``footer.html`` in the _inludes folder:

```bash
_includes/footer.html
```

Copy the entire content of the file into the project and modify intentionally.

- Avoid Minima-specific includes like:

```liquid
{% raw %}
{%- include social.html -%}
{% endraw %}
```

---

## 8. Masthead & Navigation + Spacing Adjustments (Respect the Structure)

Minimal Mistakes uses a structured masthead system built around:

- `.masthead`
- `.masthead__inner-wrap`
- `.greedy-nav`

Unlike Minima, navigation is not hardcoded in the layout — it is driven by `_data/navigation.yml` and rendered through includes.

This means:

- Styling adjustments should happen in SCSS, not layout edits  
- Navigation structure should live in data files  
- Layout overrides should be avoided unless absolutely necessary  

If spacing needs adjustment, override styles in `_custom.scss`:

Example — Reduce vertical padding:

``` scss
.masthead {
  padding-top: 0.15rem;
  padding-bottom: 0.15rem;
}

.masthead__inner-wrap {
  padding-top: 0;
  padding-bottom: 0;
}
```

**Note**: Avoid copying and modifying masthead.html unless you fully understand the include chain.
In most cases, configuration and styling are enough.

---

## 9. Blog + Archive Pages

Blog page

``` yaml
---
title: "Posts"
layout: home
permalink: /blog/
---
```

Archive page

``` yaml
---
title: "Archive"
layout: archive
permalink: /archive/
---
```

Minimal Mistakes does not use Minima's blog layout structure.

- Update incrementally and run the development server to preview changes locally:

```bash
bundle exec jekyll serve
```

---

## 10. Lessons Learned

- Disable old overrides before migrating
- Keep one PR per outcome
- Resolve conflicts on feature branches
- Let MM load default structure first
- Respect the layout hierarchy

---

## 11. What This Migration Actually Changed

- [Minima](https://datainsidedata.com/projects/jekyll-from-zero-to-production/) teaches you Jekyll.
- Minimal Mistakes teaches you structure.

The migration wasn’t just about a new theme — it was about adopting a framework that enforces discipline:

- Respect layout hierarchy
- Understand include pipelines
- Separate configuration from styling
- Override intentionally, not reactively

Minimal Mistakes doesn’t add complexity.  
It introduces architecture.

And architecture is what allows a site to scale — not just in size, but in clarity, maintainability, and professionalism.

**If you migrate intentionally**:

- Disable old overrides first  
- Let defaults load cleanly  
- Override only what you understand  
- Keep changes incremental  

You won't simply be switching themes.  
You’ll be upgrading your system design.

That’s the real shift.

Structure is not complexity.  
It’s intentional design.

---

**Data Inside Data™**  

*Tech Hands, a Science Mind, and a Heart for Community™.*
