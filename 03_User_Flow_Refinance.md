# User Flow: Refinance Journey

## Swimlanes
1. **Visitor / Homeowner**
2. **Marketing Site** (rocketmortgage.com)
3. **Rocket Application (Launchpad)**
4. **Home Loan Expert / Banker**
5. **Underwriting & Processing**

## Flow Steps

### Phase 1 — Discovery (Marketing Site lane)
1. **Visitor** lands on `/refinance` (via search, ad, or "Get rate alerts" email)
2. **Marketing Site**: Displays CTA "See what I qualify for" / refinance rate teaser
3. **Visitor** clicks CTA

### Phase 2 — Goal Identification (Launchpad lane)
4. **Launchpad**: "What are you looking to do?" → Visitor selects **Refinance**
5. **Launchpad**: Refinance goal selection (this is the key branch point):
   - **Lower my rate/payment**
   - **Cash-out (turn equity into cash)**
   - **Shorten loan term** (e.g., 30-yr → 15-yr)
   - **Consolidate debt**
   - **Remove mortgage insurance (PMI/MIP)**
6. **Decision diamond**: Goal selected →
   - **Cash-out / Debt consolidation** → branch to "Home Equity" product path (links to Home Equity sitemap section)
   - **Lower rate / Shorten term / Remove PMI** → continue standard refi path

### Phase 3 — Property & Loan Info
7. **Launchpad**: Property address (auto-pulls estimated value via AVM/public records where possible)
8. **Launchpad**: Current mortgage details — current lender, balance, rate, loan type
9. **Launchpad**: Create account / sign in (same account system as purchase flow)
10. **Launchpad**: Soft credit pull consent

### Phase 4 — Financial Profile
11. **Launchpad**: Income & employment info
12. **Launchpad**: For cash-out: desired cash amount
13. **Decision diamond**: Sufficient equity & qualification met?
    - **No** → branch to "Alternative options" (e.g., smaller cash-out amount, rate-and-term only, connect with banker)
    - **Yes** → continue

### Phase 5 — Loan Options & Selection
14. **Launchpad**: System generates refinance loan options (new rate/term combos, estimated new payment, break-even point on closing costs)
15. **Visitor**: Compares "current payment vs. new payment" side-by-side (common refi UX pattern)
16. **Visitor**: Selects preferred option
17. **Decision diamond**: Talk to a Home Loan Expert?
    - **Yes** → branch to **Home Loan Expert** lane
    - **No** → continue self-serve

### Phase 6 — Application, Appraisal & Underwriting
18. **Launchpad**: Full application + document upload (income docs, current mortgage statement, homeowners insurance info)
19. **Underwriting & Processing**: Order home appraisal (or use AVM/desktop appraisal where eligible)
20. **Decision diamond**: Appraisal value supports loan amount?
    - **No** → renegotiate loan amount/terms with **Home Loan Expert** → loop back to step 14
    - **Yes** → continue
21. **Underwriting & Processing**: Underwriting review → "Clear to close"

### Phase 7 — Closing
22. **Visitor**: Reviews Closing Disclosure (3-day TRID review period)
23. **Home Loan Expert**: Schedules closing (in-person, mobile notary, or remote online notarization)
24. **Visitor**: Signs documents
25. **Decision diamond**: Cash-out refinance?
    - **Yes** → 3-day rescission period (federally required for cash-out refis on primary residence) → funds disbursed after
    - **No** → loan funds, old loan paid off → **Refinance complete**

## Exit / Drop-off points to annotate
- After step 13 if "No equity" → exit to "Build equity" educational content or Home Equity Loan alternative
- After step 6 if goal = cash-out → consider showing this as a literal swap to the **Home Equity** product swimlane/sitemap branch — illustrates how Rocket cross-sells products based on stated goal

## Visio tips for this diagram
- Reuse the same swimlane template/shapes as the Purchase flow for visual consistency across your portfolio
- The "current payment vs. new payment comparison" (step 15) is a good candidate for a distinct shape (e.g., a small embedded table icon) — it's a unique UX element worth calling out
- Highlight the cash-out rescission period (step 25) with a note/annotation — it's a regulatory step that's easy to miss but important for IT/compliance-context audiences
