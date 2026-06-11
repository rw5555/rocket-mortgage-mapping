# Rocket Mortgage – Visio Mapping Project

## Goal
Produce two Visio deliverables based on the public rocketmortgage.com website:
1. **Site Map** – hierarchical structure of the site (org-chart style)
2. **User Flow Diagrams** – swimlane flowcharts for key user journeys

## Diagrams

### Site Map
![Site Map](01_Sitemap.drawio.png)
*Full reference: [01_Sitemap.md](01_Sitemap.md)*

### Purchase Flow
![Purchase Flow](02_User_Flow_Purchase.drawio.png)
*Full reference: [02_User_Flow_Purchase.md](02_User_Flow_Purchase.md)*

### Refinance Flow
![Refinance Flow](03_User_Flow_Refinance.drawio.png)
*Full reference: [03_User_Flow_Refinance.md](03_User_Flow_Refinance.md)*

### Research / Calculator Flow
![Research Flow](04_User_Flow_Research.drawio.png)
*Full reference: [04_User_Flow_Research.md](04_User_Flow_Research.md)*

## Scope
- Source: https://www.rocketmortgage.com (public marketing site, no login required for mapping)
- All structure below was captured by browsing the live site on 2026-06-10.
- This is a portfolio/demo project — not affiliated with or endorsed by Rocket Mortgage.

## What you'll need
- **Microsoft Visio** (Standard or Plan 2 — a free 30-day trial from Microsoft works fine for this project)
- No accounts, signups, or paid tools required to complete the planning or build the diagrams
- Optional (not required): Screaming Frog SEO Spider (free tier) if you later want to verify/expand the sitemap with a full crawl

## Files in this folder
- `01_Sitemap.md` — full site hierarchy to model as a Visio org-chart/tree diagram
- `02_User_Flow_Purchase.md` — swimlane flow for the home-purchase preapproval journey
- `03_User_Flow_Refinance.md` — swimlane flow for the refinance journey
- `04_User_Flow_Research.md` — swimlane flow for a low-intent "research/calculator" visitor

## Suggested build order
1. Build the sitemap first (simplest — straight org-chart shapes)
2. Build the purchase flow (most detailed/branching — best portfolio piece)
3. Build refinance and research flows (reuse purchase flow's swimlane template)
4. Optional: add a connector/note linking the purchase/refinance flows to "Loan options" pages in the sitemap, showing how site structure supports user journeys

## Notes for Visio build
- Use **Cross-Functional Flowchart** template (horizontal swimlanes) for the user flows
- Use **Organization Chart** template (or basic tree of rectangles) for the sitemap
- Color coding suggestion:
  - Blue = marketing/informational pages
  - Green = tools/calculators
  - Orange = application/form steps
  - Yellow decision diamonds = branch points
  - Gray = account/dashboard (post-login) areas
