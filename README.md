# EnergyPulse

A personal project building an ML-powered daily energy market signal for GCC markets — EIA price data, sentiment analysis, and a time-series model, combined into one signal.

**Status:** early development. Currently pulling and validating free EIA data (Brent, WTI, Henry Hub) before building the modeling pipeline.

## Setup
pip install -r requirements.txt

Add a `.env` file with `EIA_API_KEY=your_key_here` (free at eia.gov/opendata).

## Progress
See `notes/build_log.md`.