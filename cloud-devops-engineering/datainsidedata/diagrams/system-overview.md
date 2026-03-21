# High-Level System Architecture

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
flowchart TB

  classDef default fill:#111827,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
  classDef subgraphStyle fill:#0b1220,stroke:#3b82f6,stroke-width:2px,color:#ffffff;

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

  style Content_Layer fill:#0b1220,stroke:#3b82f6,stroke-width:2px,color:#ffffff
  style Config_Layer fill:#0b1220,stroke:#3b82f6,stroke-width:2px,color:#ffffff
  style Presentation_Layer fill:#0b1220,stroke:#3b82f6,stroke-width:2px,color:#ffffff
  ```
