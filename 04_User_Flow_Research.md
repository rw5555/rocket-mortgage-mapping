# User Flow: Low-Intent Research / Calculator Visitor

This flow represents a visitor who is "just looking" — comparing rates or estimating payments without
intent to apply immediately. Useful for showing a **lower-conversion-intent path** alongside the
high-intent Purchase and Refinance flows.

## Swimlanes
1. **Visitor**
2. **Marketing Site / Content**
3. **Calculator Tools**
4. **Rocket Application (Launchpad)** (only if visitor converts)

## Flow Steps

1. **Visitor** lands on Home, `/mortgage-rates`, or a Learn/blog article (often via organic search, e.g. "current mortgage rates")
2. **Marketing Site**: Displays "Build your estimate" widget — "I'm [buying/refinancing] and I'm currently [researching/...]"
3. **Visitor**: Selects intent (e.g., "buying" + "researching")
4. **Calculator Tools**: Displays today's rate table (30-yr fixed, 30-yr FHA, 15-yr fixed, VA, etc.) with rate/APR/points
5. **Decision diamond**: Visitor wants more detail?
   - **No** → exits site, or navigates to another page (bounce)
   - **Yes** → continue
6. **Visitor**: Clicks "Explore all calculators" or a specific calculator (mortgage payment calculator, affordability calculator, refinance calculator, amortization calculator)
7. **Calculator Tools**: Visitor inputs home price, down payment, loan term, estimated credit score, location (for tax/insurance estimates)
8. **Calculator Tools**: Displays estimated monthly payment breakdown (principal & interest, taxes, insurance, PMI if applicable)
9. **Decision diamond**: Visitor satisfied with estimate / wants to act?
   - **Exit** → visitor leaves (possible future return visit) — annotate as "soft conversion opportunity lost"
   - **Sign up for rate alerts** → captures email, no full application (low-friction conversion) → **End: Lead captured**
   - **Get my estimate / See what I qualify for** → branches into the full Purchase flow (`02_User_Flow_Purchase.md`, Phase 2)
10. **Marketing Site**: Along the way, visitor may engage with **Rocket Assist chat widget** (persistent across all pages) — branch: chat answers question → returns to same step, or chat escalates to live agent

## Content/Learn path variant
- **Visitor** arrives via a Learn/education article (e.g., "First-time buyer toolkit", "How to improve your credit score for a mortgage")
- **Marketing Site**: Article includes embedded CTAs and related-article links (internal linking — good for showing site architecture/SEO funnel design)
- **Decision diamond**: Visitor clicks related article → loops within Learn content
- **Decision diamond**: Visitor clicks CTA → branches to Calculator Tools (step 6) or directly to Purchase/Refinance flow

## Why this flow matters for the portfolio
- Demonstrates understanding that **not all site traffic is conversion-ready** — IT/UX teams design distinct paths for awareness, consideration, and decision stages
- Shows the **soft-conversion mechanism** (rate alerts/email capture) as a middle ground between "bounce" and "full application" — a common pattern in financial services sites worth highlighting
- The Rocket Assist chat widget as a cross-cutting element ties back to your sitemap note about global/persistent UI elements

## Visio tips for this diagram
- Use a lighter color palette for this flow vs. Purchase/Refinance (e.g., light blue/gray) to visually signal "lower intent" at a glance
- Show explicit "Bounce/Exit" endpoints with a distinct shape (e.g., circle or stop-sign shape) — useful contrast against the "Closing complete" endpoints in the other two flows
- Consider placing all three flow diagrams (Purchase, Refinance, Research) on one large Visio page with connectors between them at their convergence points (e.g., Research → Purchase Phase 2) to show the complete site ecosystem
