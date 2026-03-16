# DataInsideData.com Production Platform Architecture

> Part of the DataInsideData™ technical portfolio monorepo.

**Fari Lindo • DataInsideData™**

**Role:** Technical Builder — Analytics, CI/CD, Cloud Deployment, Systems Engineering, and Static Platform Architecture

---

## Domains Represented

![Platform Engineering](https://img.shields.io/badge/Platform%20Engineering-111111?logo=github&logoColor=white)
![Systems Engineering](https://img.shields.io/badge/Systems%20Engineering-111111)
![DevOps](https://img.shields.io/badge/DevOps-111111?logo=githubactions&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-111111?logo=githubactions&logoColor=white)
![Cloud Deployment](https://img.shields.io/badge/Cloud%20Deployment-111111?logo=amazonaws&logoColor=white)
![Analytics](https://img.shields.io/badge/Analytics%20Instrumentation-111111?logo=googleanalytics&logoColor=white)
![Static Platform Architecture](https://img.shields.io/badge/Static%20Platform%20Architecture-111111?logo=jekyll&logoColor=white)
![Documentation Systems](https://img.shields.io/badge/Documentation%20Systems-111111?logo=markdown&logoColor=white)

## Implementation Stack

![Jekyll](https://img.shields.io/badge/Jekyll-CC0000?logo=jekyll&logoColor=white)
![Minimal Mistakes](https://img.shields.io/badge/Minimal%20Mistakes-222222)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?logo=github&logoColor=white)
![AWS Route 53](https://img.shields.io/badge/AWS%20Route%2053-232F3E?logo=amazonaws&logoColor=white)
![GA4](https://img.shields.io/badge/Google%20Analytics%204-E37400?logo=googleanalytics&logoColor=white)
![SCSS](https://img.shields.io/badge/SCSS-CC6699?logo=sass&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white)
![Mermaid](https://img.shields.io/badge/Mermaid-Diagrams-111111)

---

## Overview

This project documents the live production platform architecture behind **DataInsideData.com**.

It is not simply a website theme implementation or front-end presentation exercise. It is a layered technical system that combines static site generation, content architecture, collection-based publishing, analytics instrumentation, continuous deployment, cloud DNS integration, and documentation-driven project rendering.

The platform is built using **Jekyll** and **Minimal Mistakes**, deployed through **GitHub Actions** and **GitHub Pages**, routed through **AWS Route 53**, and instrumented with **Google Analytics 4** in production builds.

The broader objective is to create a scalable technical publishing platform that supports multiple project domains across analytics, systems engineering, cloud workflows, and technical documentation.

---

## Executive Summary

DataInsideData.com is built as a production-oriented static publishing platform rather than a simple portfolio site.

The architecture separates authoring, build, deployment, domain routing, and analytics into clear functional layers. A private source-of-truth workflow governs editable content and implementation logic, while a public deployment repository serves the compiled hosting output for the live site.

This structure supports:

- cleaner separation of concerns
- safer publishing boundaries
- scalable project documentation workflows
- maintainable theme customization
- production-aware analytics
- future growth across multiple technical domains

This project demonstrates practical platform thinking at the intersection of analytics, CI/CD, cloud deployment, systems engineering, and structured static publishing.

---

## What This Project Demonstrates

- production static site architecture
- Minimal Mistakes migration and disciplined override strategy
- collection-based content publishing with Jekyll
- reusable include-driven project rendering
- GitHub-backed README presentation flow
- CI/CD deployment through GitHub Actions
- GitHub Pages hosting via a public build artifact repo
- custom domain routing through AWS Route 53
- production-only GA4 telemetry injection
- monorepo-friendly documentation architecture for multiple technical domains

---

## Live Platform Links

- **Live Site:** [DataInsideData.com](https://datainsidedata.com)
- **Public Deployment Repository:** [did-site-public](https://github.com/DataEden/did-site-public)
- **Monorepo Project Folder:** [DATAINSIDEDATA/](https://github.com/DataEden/fari-tech-portfolio/tree/main/DATAINSIDEDATA)

---

## Why This Project Matters

This project reflects how I approach technical systems: as layered, maintainable platforms rather than isolated files or one-off builds.

It demonstrates:

- migration planning over reactive customization
- structured content architecture over ad hoc page sprawl
- deployment automation over manual publishing
- documentation-driven workflows over duplicated content maintenance
- production-minded thinking about telemetry, hosting, and system boundaries

For hiring managers, collaborators, and technical reviewers, this project shows a practical systems view of how content, code, automation, and infrastructure fit together.

---

## Architecture at a Glance

**Diagram Placeholder — Insert system overview diagram here**

Suggested topics for this diagram:

- source content layer
- Jekyll build layer
- Minimal Mistakes presentation layer
- GitHub Actions deployment
- public build repo
- GitHub Pages
- Route 53 custom domain
- live visitor flow

---

## High-Level Platform Model

DataInsideData.com is organized into several major layers:

### 1. Content Layer
The platform includes structured publishing sources such as:

- posts
- projects
- how-tos
- fixes
- standalone pages

These content sources are designed to scale across multiple technical domains while staying organized and discoverable.

### 2. Configuration Layer
Core platform behavior is controlled through:

- `_config.yml`
- collection definitions
- defaults
- navigation data files
- analytics settings
- theme configuration

### 3. Presentation Layer
Rendering is handled through:

- Jekyll
- Minimal Mistakes layouts
- include-driven components
- SCSS overrides
- client-side README rendering for selected project pages

### 4. Build and Deployment Layer
The site is compiled and deployed through:

- GitHub Actions
- production build workflow
- compiled `_site` publishing
- public deployment repository
- GitHub Pages serving layer

### 5. Infrastructure Layer
Production delivery includes:

- Route 53 DNS management
- custom domain routing
- GitHub Pages domain mapping
- CNAME handling

### 6. Observability Layer
Analytics and telemetry are handled through:

- GA4 integration
- production-only injection
- future extensibility for event tracking

---

## Platform Architecture Diagram Placeholder

**Diagram Placeholder — Insert layered platform architecture diagram here**

Suggested topics:

- Content Layer
- Config Layer
- Presentation Layer
- Build Layer
- Deployment Layer
- DNS / Delivery Layer
- Analytics Layer

---

## Two-Repository Deployment Model

A key architectural decision in this platform is the separation of authoring from deployment.

### Private Source-of-Truth Layer
The editable implementation lives in the source repository and includes:

- content
- layouts
- includes
- SCSS
- assets
- configuration
- workflow logic

### Public Deployment Layer
The public repository exists to serve compiled output for hosting.

This repository functions as the deployment artifact layer rather than the primary authoring environment.

### Why this matters

This separation improves:

- maintainability
- deployment clarity
- source control discipline
- reduced exposure of internal-only materials
- professional publishing structure

---

## Deployment Flow Placeholder

**Diagram Placeholder — Insert deployment flow diagram here**

Suggested flow:

- private source repo
- push to main
- GitHub Actions workflow
- production Jekyll build
- `_site` output
- push to public repo
- GitHub Pages
- Route 53 custom domain
- live site

---

## Monorepo + Project Rendering Model

This platform supports a monorepo-style workflow where individual project folders can maintain their own documentation and be surfaced into the site.

For selected project pages, the website dynamically retrieves a README from a repository subfolder and renders it into the page through custom include components.

This allows the repository to remain the single source of truth while the website acts as the presentation layer.

### Benefits of this approach

- reduces duplicated documentation
- keeps project documentation synchronized
- supports consistent project presentation
- scales well across multiple technical domains
- aligns with portfolio-as-platform thinking

---

## Documentation Rendering Flow Placeholder

**Diagram Placeholder — Insert README rendering flow diagram here**

Suggested flow:

- monorepo subfolder
- README.md
- raw GitHub URL
- custom include
- marked.js
- rendered project page inside Minimal Mistakes

---

## Minimal Mistakes and Theme Strategy

Minimal Mistakes was chosen not simply for aesthetics, but for architecture.

It provides:

- collection support
- structured layouts
- responsive navigation
- search support
- TOC support
- archive patterns
- author profile options
- scalable theme conventions

The project follows a deliberate override strategy:

- let the theme load clean defaults first
- avoid local include collisions from legacy themes
- override intentionally rather than reactively
- centralize styling in SCSS rather than scattered CSS fragments

This allowed the platform to move from a simpler learning-stage setup toward a more maintainable publishing framework.

---

## Theme / Rendering Architecture Placeholder

**Diagram Placeholder — Insert theme dependency or rendering diagram here**

Suggested flow:

- markdown content
- front matter
- layout
- includes
- custom includes
- SCSS
- rendered HTML
- final compiled site

---

## Analytics and Observability

The platform integrates **Google Analytics 4** as part of the production publishing architecture.

Analytics configuration is controlled through Jekyll config and is injected only when the build environment is set to production. This prevents local development traffic from polluting live measurement.

### What this demonstrates

- production-aware telemetry handling
- clean separation between local development and live analytics
- observability as part of platform design
- future readiness for richer event instrumentation

### Current and future telemetry scope

Current or planned observability use cases include:

- page views
- traffic sources
- user navigation behavior
- project page engagement
- outbound repository click tracking
- future event-level instrumentation

---

## Analytics Flow Placeholder

**Diagram Placeholder — Insert analytics and observability diagram here**

Suggested flow:

- visitor
- live site
- GA4 script
- analytics property
- dashboards / insight loop

---

## Key Technical Components

- **Jekyll** for static site generation
- **Minimal Mistakes** for structured theme architecture
- **GitHub Actions** for automated build and deploy workflows
- **GitHub Pages** for static hosting
- **AWS Route 53** for DNS and custom domain routing
- **GA4** for production telemetry
- **SCSS** for maintainable theme-aware styling
- **Markdown + README workflows** for documentation-driven publishing
- **Custom include components** for GitHub-backed project presentation

---

## Repository Structure

```text
DATAINSIDEDATA/
├─ README.md
├─ docs/
│  ├─ architecture-notes.md
│  ├─ migration-notes.md
│  └─ deployment-notes.md
├─ diagrams/
│  ├─ system-overview.md
│  ├─ deployment-flow.md
│  ├─ rendering-flow.md
│  └─ analytics-flow.md
├─ images/
│  ├─ hero-platform-visual.png
│  ├─ platform-overview.png
│  └─ deployment-diagram.png
└─ references/
   ├─ config-snippets.md
   └─ workflow-snippets.md