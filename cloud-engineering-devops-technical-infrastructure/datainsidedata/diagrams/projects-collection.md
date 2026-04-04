# Collection Architecture

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "background": "#0b1220",
    "lineColor": "#3b82f6",
    "fontSize": "18px",
    "fontFamily": "Arial",
    "textColor": "#ffffff",
    "primaryTextColor": "#ffffff",
    "secondaryTextColor": "#e5e7eb"
  }
}}%%
flowchart LR

classDef default fill:#111827,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
classDef subgraphStyle fill:#0b1220,stroke:#3b82f6,stroke-width:2px,color:#ffffff;

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
