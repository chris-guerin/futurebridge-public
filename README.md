# futurebridge-public

Public-facing pages for FutureBridge Advisory, served via GitHub Pages.

**This repo is public. Committing to it is publishing.**

## What belongs here

Only material intended for the open web: method and positioning pages,
general thought-leadership, and the index that links them.

## What must never be committed here

- Contact data of any kind — names, work emails, job titles, LinkedIn URLs
- Client lists, or any page that names who the clients are
- Per-client intelligence briefs, account plans, dashboards, scores or rationales
- Anything exported from the Signal Engine (`signal_engine_*.csv`, deliverables,
  recipient lists, outreach files)
- Credentials, connection strings, API keys

Client-confidential work lives in the private `workfiles-` repo and stays there.

## Guard

`.githooks/pre-commit` blocks commits containing email addresses (other than
`@futurebridge.com`), LinkedIn profile URLs, or known client names. Enable it once
per clone:

    git config core.hooksPath .githooks

The hook is a backstop, not a substitute for reading what you are committing.

## Contents

| File | Notes |
|---|---|
| `index.html` | Landing page |
| `FutureBridge_Method_Credibility.html` | The method |
| `uk-energy-sovereign-case.html` | Energy sovereignty |
| `mobility-infographic.html` | Who gets the money? |
