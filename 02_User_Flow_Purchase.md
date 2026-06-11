# User Flow: Home Purchase Preapproval Journey

## Swimlanes
1. **Visitor / Applicant**
2. **Marketing Site** (rocketmortgage.com)
3. **Rocket Application (Launchpad)**
4. **Home Loan Expert / Banker**
5. **Underwriting & Processing**

## Flow Steps

### Phase 1 — Discovery (Marketing Site lane)
1. **Visitor** lands on Home or `/purchase` page (via search, ad, or direct)
2. **Marketing Site**: Displays hero CTA "See what I qualify for" / "Start my preapproval"
3. **Visitor** clicks CTA
4. **Decision diamond**: Already has a Rocket account?
   - **Yes** → branch to Sign In → skip to Phase 3 (pre-filled)
   - **No** → continue to Phase 2

### Phase 2 — Account Creation & Initial Qualification (Launchpad lane)
5. **Launchpad**: "What are you looking to do?" → Visitor selects **Buy a home**
6. **Launchpad**: Property details — state/location, property type (single-family, condo, multi-unit), intended use (primary residence, second home, investment)
7. **Launchpad**: Purchase timeline — "When do you want to buy?" (Researching / 1-3 months / Under contract / etc.)
8. **Decision diamond**: "Already have an agent / found a home?"
   - **Yes** → capture property address/MLS info
   - **No** → continue generic
9. **Launchpad**: Create account — email, phone, password (or continue via Google/Apple)
10. **Launchpad**: Soft credit pull consent (explicitly "won't affect your credit score")

### Phase 3 — Financial Profile (Launchpad lane)
11. **Launchpad**: Income & employment info (employer, income type, length of employment)
12. **Launchpad**: Assets / down payment amount
13. **Launchpad**: Estimated credit score range (if soft pull not completed) or actual soft-pull result
14. **Decision diamond**: Does applicant meet minimum qualification thresholds?
    - **No / Marginal** → branch to "Alternative options" (e.g., FHA loan suggestion, credit-improvement resources, connect with banker for manual review)
    - **Yes** → continue

### Phase 4 — Loan Options & Preapproval (Launchpad lane)
15. **Launchpad**: System generates personalized loan options (rate/term combinations: 30-yr fixed, 15-yr fixed, ARM, FHA, VA if applicable)
16. **Visitor**: Reviews and selects preferred loan option
17. **Launchpad**: Generates **Preapproval Letter** (PDF, downloadable/shareable)
18. **Decision diamond**: Visitor wants to talk to a person?
    - **Yes** → branch to **Home Loan Expert** lane: schedule call / connect now
    - **No** → continue self-serve

### Phase 5 — Full Application & Document Collection
19. **Visitor**: Continues to full mortgage application (if moving from preapproval to active loan)
20. **Launchpad**: Document upload portal — pay stubs, W-2s/1099s, bank statements, ID
21. **Home Loan Expert**: Reviews submitted docs, requests any missing items (loop back to step 20 if incomplete)

### Phase 6 — Underwriting & Closing
22. **Underwriting & Processing**: Automated + manual underwriting review
23. **Decision diamond**: Approved as submitted?
    - **No** → "Conditional approval" → request additional documentation → loop back to step 20
    - **Yes** → continue
24. **Underwriting & Processing**: "Clear to close" status
25. **Visitor**: Reviews Closing Disclosure (3-day review period per TRID regulations)
26. **Home Loan Expert**: Schedules closing (in-person, mobile notary, or remote online notarization)
27. **Visitor**: Signs closing documents → loan funds → **Closing complete**

## Exit / Drop-off points to annotate
- After step 7 (timeline = "just researching") → likely exits to Learn/education content (link to `04_User_Flow_Research.md`)
- After step 14 if "No" and no alternative accepted → exit to educational resources / "improve your credit" content
- Step 18 "No" → stays fully self-serve through Launchpad without ever speaking to a banker (notable UX path worth calling out)

## Visio tips for this diagram
- Use a **rounded rectangle** for marketing/content pages, **rectangle** for application/system steps, **diamond** for decisions, **document shape** for the Preapproval Letter and Closing Disclosure
- Color the "Phase" bands as vertical or horizontal zones across the swimlanes (Visio supports phase markers in Cross-Functional Flowchart)
- Add a callout box referencing "Zero credit impact" messaging at step 10 — this is a key UX/marketing detail Rocket emphasizes repeatedly on the site
