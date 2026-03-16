---


---

# DataInsideData Blog — Site & System Architecture & Design Specification

## 1) High-Level System Architecture

```mermaid
flowchart TB
  U[Site Owner / Contributor] --> C[Content Sources]

  subgraph Content_Layer[Content Layer]
    P[_posts]
    PR[_projects]
    H[_how_tos]
    F[_fixes]
    SP[Standalone Pages]
  end

  subgraph Config_Layer[Configuration Layer]
    CFG[_config.yml]
    NAV[_data/navigation.yml]
  end

  subgraph Presentation_Layer[Presentation Layer]
    MM[Minimal Mistakes Theme]
    INC[_includes]
    SCSS[assets/css/main.scss]
    CUSTOM[_sass/minimal-mistakes/_custom.scss]
    JS[assets/js/mermaid-init.js]
    IMG[assets/images]
  end

  C --> P
  C --> PR
  C --> H
  C --> F
  C --> SP

  P --> J[Jekyll Build Engine]
  PR --> J
  H --> J
  F --> J
  SP --> J

  CFG --> J
  NAV --> J
  MM --> J
  INC --> J
  SCSS --> J
  CUSTOM --> J
  JS --> J
  IMG --> J

  J --> SITE[_site Compiled Static Site]

  SITE --> GA[GitHub Actions Deploy Workflow]
  GA --> PUB[Public Repo: did-site-public]
  PUB --> GHP[GitHub Pages / gh-pages]
  GHP --> DNS[Route 53 + datainsidedata.com]
  DNS --> V[Site Visitor]
  ```

**What this diagram shows**

- The Site is organized into clear layers: content, configuration, presentation, build, and deployment.
- Jekyll compiles all markdown, config, theme logic, includes, styles, and scripts into _site.
- Deployment is separated from authoring through the two-repo strategy (separation of concerns).

**Why it matters**

- This is the best “executive view” of the system.
- It helps future contributors understand where content lives versus how the site is rendered and shipped.

## 2) Public Site Map / Navigation Flow

```mermaid
flowchart TD
  HOME[Start Here /]
  BLOG[Posts /blog/]
  PROJECTS[Projects /projects/]
  HOWTOS[How Tos /how-tos/]
  FIXES[Fixes /fixes/]
  ABOUT[About /about/]
  CONTACT[Contact /contact/]
  ARCHIVE[Archive /archive/]
  PRIVACY[Privacy /privacy/]
  TERMS[Terms /terms/]
  NOTFOUND[404 Page]

  HOME --> BLOG
  HOME --> PROJECTS
  HOME --> HOWTOS
  HOME --> FIXES
  HOME --> ABOUT
  HOME --> CONTACT

  BLOG --> ARCHIVE
  BLOG --> PRIVACY
  BLOG --> TERMS

  PROJECTS --> PROJECT_DETAIL[Project Detail Pages]
  HOWTOS --> HOWTO_DETAIL[How-To Detail Pages]
  FIXES --> FIX_DETAIL[Fix Detail Pages]
  BLOG --> POST_DETAIL[Post Detail Pages]

  ARCHIVE --> POST_DETAIL
```

**What this diagram shows**

- The homepage is the landing page, while /blog/ is the posts hub.
- Collections each have a hub page and then detail pages underneath.
- Legal and utility pages support the site but are not primary discovery hubs.
  - they are placed on the footer and the footer-bottom.

**Why it matters**

- This is the visitor-facing navigation model.
- It is useful for both UX planning and contributor onboarding.

## 3) Collection Architecture

```mermaid
flowchart LR
  POSTS_SRC[_posts] --> POSTS_HUB[/blog/]
  POSTS_SRC --> POST_PAGES[Blog Post Pages]

  PROJECTS_SRC[_projects] --> PROJECTS_HUB[/projects/]
  PROJECTS_SRC --> PROJECT_PAGES[Project Pages]

  HOWTOS_SRC[_how_tos] --> HOWTOS_HUB[/how-tos/]
  HOWTOS_SRC --> HOWTO_PAGES[How-To Pages]

  FIXES_SRC[_fixes] --> FIXES_HUB[/fixes/]
  FIXES_SRC --> FIX_PAGES[Fix Pages]
```

**What this diagram shows**

- Each collection has a source folder and a public-facing hub.
- The hub and the item pages are separate concepts.
- Jekyll generates item pages from collection entries.

**Why it matters**

- This makes it easier to explain where to place new content.
- It also helps maintain clean boundaries between content types.

## 4) Standalone Page Architecture

```mermaid
flowchart TD
  ROOT[Standalone Pages]

  ROOT --> START[Start Here /]
  ROOT --> ABOUT[About /about/]
  ROOT --> CONTACT[Contact /contact/]
  ROOT --> ARCHIVE[Archive /archive/]
  ROOT --> PRIVACY[Privacy /privacy/]
  ROOT --> TERMS[Terms /terms/]
  ROOT --> ERR[404 Page]
```

**What this diagram shows**

- These pages are not part of collections.
- They serve either informational, navigational, legal, or utility purposes.
- They are managed as individual pages rather than repeated content patterns.

**Why it matters**

- This helps separate “site structure pages” from “content publishing pages.”
- It is especially useful for future staff and contributors.

## 5) Section Navigation Diagram

```mermaid
flowchart TD
  MAIN[Main Navigation]

  MAIN --> START[Start Here]
  MAIN --> POSTS[Posts]
  MAIN --> PROJECTS[Projects]
  MAIN --> HOWTOS[How Tos]
  MAIN --> FIXES[Fixes]
  MAIN --> ABOUT[About]
  MAIN --> CONTACT[Contact]

  HOWTOS --> AWS[AWS]
  HOWTOS --> GITHUB[GitHub]
  HOWTOS --> WINDOWS[Windows]

  FIXES --> CONDA[Conda]
  FIXES --> JEKYLL[Jekyll]
  FIXES --> PYTHON[Python]
```

**What this diagram shows**

- The primary top-level nav is concise and brand-friendly.
- The secondary navs organize How Tos and Fixes by topic families.
- Navigation is intentionally layered rather than flat.

**Why it matters**

- This gives contributors a quick mental model of site taxonomy.
- It also helps spot future expansion points.

## 6) Rendering / Theme Dependency Diagram

```mermaid
flowchart TB
  PAGE[Markdown Page or </br>Collection Item] --> FM[Front Matter]
  FM --> LAYOUT[Minimal Mistakes Layout]
  LAYOUT --> INC[_includes]

  INC --> FOOTER[footer.html Override]
  INC --> GHPROJ[github-project.html]
  INC --> GHREADME[github-readme.html]

  SCSS_ENTRY[assets/css/main.scss] --> MM_SKIN[MM Skin Import]
  SCSS_ENTRY --> MM_THEME[Minimal Mistakes </br>Theme Import]
  SCSS_ENTRY --> CUSTOM_SCSS[_sass/minimal-mistakes/_custom.scss]

  JS_INIT[assets/js/mermaid-init.js] --> MERMAID[Mermaid Rendering]

  LAYOUT --> OUTPUT[Rendered HTML]
  FOOTER --> OUTPUT
  GHPROJ --> OUTPUT
  GHREADME --> OUTPUT
  CUSTOM_SCSS --> OUTPUT
  MERMAID --> OUTPUT
```

**What this diagram shows**

- Minimal Mistakes provides layout structure.
- local includes extend the theme without replacing the whole layout system.
- Styling flows through main.scss into MM imports and the custom overrides.

**Why it matters**

- This is the clearest view of how customization layer sits on top of the theme.
- It makes future debugging much easier.

## 7) Content Publishing Flow

```mermaid
flowchart TD
  AUTHOR[Write Markdown Content] --> FRONTMATTER[Add Front Matter]
  FRONTMATTER --> TYPE{Content Type?}

  TYPE -->|Post| POSTS[_posts]
  TYPE -->|Project| PROJECTS[_projects]
  TYPE -->|How-To| HOWTOS[_how_tos]
  TYPE -->|Fix| FIXES[_fixes]
  TYPE -->|Standalone| PAGES[Standalone Page]

  POSTS --> BUILD[Jekyll Build]
  PROJECTS --> BUILD
  HOWTOS --> BUILD
  FIXES --> BUILD
  PAGES --> BUILD

  BUILD --> HTML[Generated HTML in _site]
  HTML --> DEPLOY[Deployment Pipeline]
  DEPLOY --> LIVE[Live Website]
```

**What this diagram shows**

- All content types follow the same lifecycle: write, classify, build, deploy.
- Front matter is the key control point for layout and metadata.
- Jekyll normalizes everything into static output.

**Why it matters**

- This is best contributor-facing authoring workflow diagram.
- It supports SDLC and content governance.

## 8) Deployment Flow — Two Repo Strategy

```mermaid
flowchart TB
  SRC[Private Source Repo] --> PUSH[Push to main]
  PUSH --> ACTIONS[GitHub Actions Workflow]
  ACTIONS --> BUILD[Jekyll Production Build]
  BUILD --> CNAME[Write CNAME to _site]
  CNAME --> VERIFY[Sanity Checks]
  VERIFY --> PUBLISH[Push _site to Public Repo]
  PUBLISH --> PUBLIC[Public Repo: did-site-public]
  PUBLIC --> GHPAGES[gh-pages Branch]
  GHPAGES --> DOMAIN[datainsidedata.com via Route 53]
```

**What this diagram shows**

- Source authoring and public hosting are intentionally separated.
- GitHub Actions compiles the site and publishes only the built artifact.
- The public repo acts as the serving layer rather than the authoring layer.

**Why it matters**

- This is a strong professional deployment architecture.
- It reduces accidental exposure of source-only material and keeps hosting clean.

## 9) Public vs Internal Workspace Diagram

```mermaid
flowchart TB
  WORKSPACE[Project Workspace]

  WORKSPACE --> PUBLIC[Public Build Inputs]
  WORKSPACE --> INTERNAL[Internal / Non-Build Assets]

  PUBLIC --> POSTS[_posts]
  PUBLIC --> PROJECTS[_projects]
  PUBLIC --> HOWTOS[_how_tos]
  PUBLIC --> FIXES[_fixes]
  PUBLIC --> PAGES[Standalone Pages]
  PUBLIC --> CONFIG[_config.yml]
  PUBLIC --> NAV[_data/navigation.yml]
  PUBLIC --> INCLUDES[_includes]
  PUBLIC --> STYLES[SCSS/CSS/JS]
  PUBLIC --> IMAGES[Public Assets]

  INTERNAL --> DRAFTS[_drafts]
  INTERNAL --> DOCS[docs]
  INTERNAL --> RAW[raw/source folders]
  INTERNAL --> BACKUPS[backup files]
  INTERNAL --> LOCALONLY[ignored local artifacts]
```

**What this diagram shows**

- Not everything in your repo/workspace is part of the public site.
- Internal folders support drafting, documentation, and source preservation.
- Build inputs and maintainer-only artifacts should stay conceptually separate.

**Why it matters**

- This helps contributors avoid touching the wrong areas.
- It also supports cleaner repo hygiene and long-term maintainability.

## 10) Generated Pages / Utility Architecture

```mermaid
flowchart TD
  SITE[Jekyll Site Build] --> FEED[feed.xml]
  SITE --> SITEMAP[sitemap.xml]
  SITE --> ROBOTS[robots.txt]
  SITE --> PAGINATION[Paginated Blog Pages]
  SITE --> ERR[404 Page]
  SITE --> ARCHIVE[Archive Page]
  SITE --> SEARCH[Lunr Search Index]
  SITE --> TAGS[Future Tags Page]
```

**What this diagram shows**

- Some important site outputs are generated or utility-oriented.
- These pages support discovery, navigation, crawling, and user recovery.
- The future tags page fits naturally into this supporting architecture.

**Why it matters**

- This is key for SEO, findability, and content operations.
- It also shows that the site is more than a collection of markdown pages.

## 11) Future Tags Architecture

```mermaid
flowchart TD
  POSTS[Blog Posts] --> TAGS_META[Tags in Front Matter]
  TAGS_META --> TAGS_INDEX[/tags/]
  TAGS_INDEX --> TAG_GROUPS[Grouped Tag Sections]
  TAG_GROUPS --> RELATED_POSTS[Linked Post Lists]
  ARCHIVE[/archive/] --> TAGS_INDEX
  BLOG[/blog/] --> TAGS_INDEX
```

**What this diagram shows**

- Posts declare tags in front matter.
- A /tags/ page can act as a taxonomy index.
- That page can connect back into blog discovery and archive browsing.

**Why it matters**

- This is the cleanest MM-friendly way to improve content discoverability.
- It supports internal linking, topical clustering, and better browsing behavior.

**Notes**

- Use a master /tags/ page with grouped sections first.
- Later, if needed, expand toward more advanced tag archive behavior.

## 12) GitHub Project Embed Flow

```mermaid
flowchart TD
  PROJECT_PAGE[Project Page] --> INCLUDE[github-project.html Include]
  INCLUDE --> API[GitHub Repo API]
  INCLUDE --> README_RAW[Raw README URL]
  README_RAW --> MARKED[marked.js Markdown Parser]
  API --> META[Repo Metadata Rendered]
  MARKED --> README_HTML[README Rendered in Page]
  META --> FINAL[Enhanced Project Presentation]
  README_HTML --> FINAL
```

**What this diagram shows**

- Your project pages can dynamically enrich themselves with GitHub data.
- Repo metadata and README content are fetched separately.
- The rendered result becomes a richer project showcase page.

**Why it matters**

- This is a strong portfolio feature.
- It also documents a custom behavior future contributors would not know from theme defaults alone.

# 13) Analytics & Observability Architecture

```mermaid
flowchart TB
  VISITOR[Site Visitor] --> SITE[datainsidedata.com]

  SITE --> SCRIPT[Google gtag Script]

  SCRIPT --> GA4[Google Analytics Property]

  GA4 --> DASH[Analytics Dashboard]

  DASH --> INSIGHTS[Traffic + Behavior Insights]
```

**What this diagram shows**

- When a visitor loads a page, the gtag script runs in the browser.
- The script sends pageview and event data to the Google Analytics property.
- The analytics dashboard aggregates that telemetry for reporting.

**Why it matters**

- This provides observability into how the site is used.
- It supports decisions about content strategy, SEO performance, and site navigation.

## Configuration Architecture (Analytics)

The _config.yml entry is the control point:

```bash
analytics:
  provider: "google-gtag"
  google:
    tracking_id: "G-XXXXXXX"
    anonymize_ip: true
```

**What this configuration does**

- provider: `google-gtag`
Enables the `GA4` tracking integration built into Minimal Mistakes.

- `tracking_id`
Connects the site to your specific Google Analytics property.

- `anonymize_ip: true`
Enables IP anonymization for privacy compliance.

**How Jekyll activates analytics**

- This part is important for the architecture explanation.

DID's GitHub Actions workflow sets:

```yml
env:
  JEKYLL_ENV: production
```

During build:

```yml
bundle exec jekyll build
```

**Minimal Mistakes only injects analytics scripts when**:

```yml
JEKYLL_ENV == production
```

## 14) Flow Chart

```mermaid
flowchart TD
  CONFIG[_config.yml <br/>analytics settings] --> BUILD[Jekyll Build]

  BUILD --> CHECK{JEKYLL_ENV == production?}

  CHECK -->|Yes| INJECT[Inject gtag Script]
  CHECK -->|No| SKIP[Skip Analytics Script]

  INJECT --> SITE[Compiled Static Site]
  SITE --> VISITOR[Visitor Browser]

  VISITOR --> GA4[Google Analytics]
```

**Why this is important**

- Analytics does not run during local development
- It only runs in production builds
- This prevents test traffic from polluting metrics

That is exactly how production analytics behaves in an enterprise environment.

## Analytics & Telemetry

The site integrates Google Analytics via the Minimal Mistakes google-gtag provider.
Tracking is configured in _config.yml and injected into the site during production builds.

Analytics scripts are only included when the environment variable JEKYLL_ENV=production is set. This ensures development and preview builds do not send telemetry data.

**Collected analytics data includes**:

- page views
- traffic sources
- geographic distribution
- device types
- user navigation paths
- IP anonymization is enabled for privacy compliance.

## 15) Small pro-level improvement (optional)

Later add an Event Tracking layer.

Example events:

- project page views
- GitHub repo clicks
- outbound link clicks
- tutorial completion

**Architecture addition**:

```mermaid
flowchart LR
  USER --> PAGE[Project Page]
  PAGE --> EVENT[Custom Event]
  EVENT --> GA4[Google Analytics Events]
```

This turns analytics from passive measurement into product insight.

The site now includes all major production-grade layers:

- content model
- presentation framework
- CI/CD pipeline
- custom component system
- analytics telemetry
- SEO infrastructure

That’s a very complete architecture for a modern static site.

## Positions for diagrams in the document

Order:

- System Overview
- Public Site Architecture
- Content Architecture
- Rendering / Theme Architecture
- Publishing Workflow
- Deployment Architecture
- Analytics & Observability
- SEO / Discovery Systems
- Future Enhancements

**Data Inside Data™.**
