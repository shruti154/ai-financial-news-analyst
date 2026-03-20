# AI Financial News Analyst

A prompt-engineered AI tool that analyses global financial 
news headlines for two user types: Fintech Analysts and 
Retail Investors. Tested across UK (BoE), Europe (ECB), 
and US (Fed) markets.

---

## The Problem

Financial news moves fast. A retail investor and a fintech 
analyst read the same headline — but need completely 
different things from it.

No existing tool serves both users from the same input 
without requiring technical knowledge or financial literacy.

---

## What This Project Does

Takes a financial news headline as input and returns a 
structured brief in two parallel modes:

**Analyst Mode** — Technical depth, source attribution, 
forward-looking signals, confidence scoring, up to 4 
risk flags

**Retail Mode** — Plain English, one practical implication, 
maximum 1 risk flag, no jargon

---

## Key Design Decisions

- **Refuse over hallucinate** — model returns 
  "insufficient data" rather than fill gaps with inference
- **Trust as core metric** — success measured by 
  hallucination rate and source accuracy, not DAU
- **Historical data flagging** — stale headlines 
  automatically identified and labelled

---

## Eval Results

| Version | Avg Score (/30) | Key Gap |
|---|---|---|
| V1 | 23.0 | No source attribution, single mode |
| V2 | 29.7 | Minor hallucination (ECB test) |

**Improvement: +29% from one prompt iteration**

Markets tested: Bank of England, ECB, Federal Reserve

---

## Files & Links

| Resource | Description | Link |
|---|---|---|
| `prompt-v1.txt` | Original prompt — single mode | In this repo |
| `prompt-v2.txt` | Improved prompt — dual mode | In this repo |
| Eval Sheet | Full scoring across 6 experiments | [View on Google Sheets](https://docs.google.com/spreadsheets/d/1psYPl1K0IxWjlVeHw3E_a9ZBH9mWWYA1XHVDfXiwhss/edit?gid=0#gid=0) |
| Project Log | Product brief, experiments, case study | [View on Notion](https://www.notion.so/AI-Financial-News-Analyst-ede5c7b1afba4487893c20dd964b8b4e?source=copy_link)


---

## What I'd Build Next

- **RAG layer** — connect to live news feeds and central 
  bank press releases
- **Contradiction detection** — flag when two sources 
  report the same event differently  
- **Portfolio personalisation** — retail mode surfaces 
  only news relevant to stocks the user holds

---
