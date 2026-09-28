Running log of what was built, what broke, and what fixed it. Written for you in six months, not for an audience — short and honest beats polished.

## [date] — Day 1: environment + first EIA API call
- Registered an EIA API key at eia.gov/opendata
- Set up the local project folder and Python environment in VS Code
- Wrote a first version of fetch_data.py

## [date] — Debugging session
- Hit `SyntaxError: unterminated triple-quoted string literal` — an unmatched `'''` somewhere in the file. Found it by counting `'''` occurrences until one didn't have a pair.
- Hit `API_KEY_MISSING` even with a `.env` file present — python-dotenv wasn't picking it up. Fixed by [confirm and fill in: was it the Windows hidden .env.txt extension, or a working-directory mismatch?]
- Moved the API key fully into `.env`, confirmed it's excluded via `.gitignore`.

## [date] — First real data pull
- Got a working response from `petroleum/pri/spt` — Brent, WTI, and nine US refined-product spot price series, 2020–present.
- Ran `.unique()` on `series-description` to see what's actually in the dataset rather than assume.
- Finding: no Dubai crude, no TTF, no JKM here — those are proprietary Platts/ICE/DME data, not free anywhere. Henry Hub isn't in this endpoint either — it's under a separate `natural-gas` API route.
- Decision: v0 data set is Brent + WTI + Henry Hub, not the original five commodities from the playbook.

## [date] — your next entry