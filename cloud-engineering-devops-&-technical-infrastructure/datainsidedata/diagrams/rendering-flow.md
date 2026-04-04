# GitHub Project Embed Flow

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
flowchart TD

classDef default fill:#111827,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
classDef subgraphStyle fill:#0b1220,stroke:#3b82f6,stroke-width:2px,color:#ffffff;

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

- Project pages can dynamically enrich themselves with GitHub data.
- Repo metadata and README content are fetched separately.
- The rendered result becomes a richer project showcase page.

**Why it matters**

- This is a strong portfolio feature.
- It also documents a custom behavior future contributors would not know from theme defaults alone.
