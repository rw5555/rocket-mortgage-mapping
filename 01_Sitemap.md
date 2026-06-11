# Rocket Mortgage – Site Map (for Visio Org-Chart Diagram)

Captured from the live header navigation and landing pages (2026-06-10). Build this as a tree:
**Home (root)** → top-level nav sections → sub-pages.

## Home (rocketmortgage.com)
- Hero CTA: "See what I qualify for" → leads into Purchase application flow
- Secondary CTAs: "See today's rates", "Build your estimate" (rate calculator widget)

## 1. Buy
- Buy a home (`/purchase`)
- Get started / Start preapproval (`/purchase/get-started`)
- Calculators
- Learn (buying education hub)
- Español (buy section)
- **Popular links:**
  - Purchase loan options
  - VA & military purchase resources (`/purchase/va-military-homebuyer`)
  - First-time homebuyer resources (`/purchase/first-time-homebuyer`)
  - Rocket Mortgage & Redfin savings
  - Chat (Rocket Assist)

## 2. Refinance
- Refinance a home (`/refinance`)
- Get started (`/refinance/get-started`)
- Calculators
- Learn (refinance education hub)
- Español (refinance section)
- **Popular links:**
  - Refinance loan options
  - VA & military refi resources
  - Debt consolidation
  - Chat (Rocket Assist)

## 3. Home Equity
- Access home equity (`/home-equity`)
- Calculators
- Learn (home equity education hub)
- Get started
- **Popular links:**
  - Home Equity Loan
  - Cash-out refinance
  - Debt consolidation
  - Chat (Rocket Assist)

## 4. Rates
- Today's rates (`/mortgage-rates`)
- Purchase rates
- Refinance rates
- Rate calculator / "Build your estimate" tool
- Mortgage rate trends / education content

## 5. Loan Options
- All home loans (overview)
- Personal loans
- **By product (Popular):**
  - 15-year fixed
  - 30-year fixed
  - Adjustable-rate mortgage (ARM)
  - Bridge loan
  - Cash-out refinance
  - VA loan
  - Home Equity Loan
  - HomeReady® / Home Possible®
  - Jumbo / Jumbo Smart

## 6. Account / Utility (top-right header)
- Sign in → Launchpad (account dashboard, requires login — `launchpad.rocketmortgage.com`)
- Apply now (CTA → application flow)
- Phone number / contact
- "Let's chat" (Rocket Assist chatbot widget — appears site-wide)

## 7. Footer-level pages (typical for this site type — verify when building)
- About Rocket Mortgage / Rocket Companies
- Careers
- Press / Newsroom
- Investor Relations
- Legal: Licensing, Privacy Policy, Terms of Use, Accessibility
- Help / Contact Us / FAQ
- Mortgage glossary / education blog (Learn center)
- Espanol (site-wide language toggle)

## Diagram structure suggestion
```
Home
├── Buy
│   ├── Buy a Home (overview)
│   ├── Get Started (preapproval)
│   ├── Calculators
│   ├── Learn
│   └── Popular (VA, First-Time Buyer, Redfin, Chat)
├── Refinance
│   ├── Refinance a Home (overview)
│   ├── Get Started
│   ├── Calculators
│   ├── Learn
│   └── Popular (VA Refi, Debt Consolidation, Chat)
├── Home Equity
│   ├── Access Home Equity (overview)
│   ├── Calculators
│   ├── Learn
│   └── Popular (HEL, Cash-Out Refi, Debt Consolidation, Chat)
├── Rates
│   ├── Purchase Rates
│   ├── Refinance Rates
│   └── Rate Calculator
├── Loan Options
│   ├── All Home Loans
│   ├── Personal Loans
│   └── By Product (15yr, 30yr, ARM, Bridge, Cash-Out, VA, HEL, HomeReady, Jumbo)
├── Account
│   ├── Sign In → Launchpad (gated)
│   └── Apply Now (CTA)
└── Footer
    ├── About / Careers / Press / Investors
    ├── Legal (Privacy, Terms, Licensing, Accessibility)
    └── Help / Learn Center / Glossary
```

## Notes
- The "Get Started" and "Apply Now" CTAs across Buy/Refinance/Home Equity all funnel into the **same underlying application flow** (Launchpad) — in your sitemap, consider drawing these as separate entry points that converge into one "Application/Launchpad" node, visually showing the funnel structure.
- "Chat (Rocket Assist)" appears as a persistent widget across nearly every page — represent this as a global element (e.g., a small icon attached to every section) rather than a single page.
