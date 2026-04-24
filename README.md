# NBA Player Impact & Value Analytics Pipeline

## Live Dashboard
(https://app.powerbi.com/view?r=eyJrIjoiODA1MjVkODUtNGE3Zi00MmIwLTljYjUtMmQ2ZmFjNDMxM2E4IiwidCI6ImFjMjRjMTRiLTc3YTEtNDZmYy1hOTY5LTkwNDRiYTIzMTc0MyJ9)

---

## Overview

This project builds an end-to-end data pipeline that transforms raw NBA data into a structured analytics dataset used to evaluate player performance and contract efficiency.

Using Python for data processing and Power BI for visualization, the project introduces custom metrics to provide a more complete view of player impact beyond traditional box score statistics.

---

## Problem

Traditional NBA statistics (points, rebounds, assists) do not fully capture a player’s overall contribution or value relative to their contract.

This project addresses that gap by combining:
- Production
- Efficiency
- Usage
- Advanced metrics
- Salary data

into a unified evaluation framework.

---

## Data Sources

Data was collected from Basketball Reference:

- Per-game player statistics  
- Advanced player statistics  
- Player salary data  

---

## Pipeline Architecture
Basketball Reference
↓
Python (pandas)
↓
Data Cleaning & Transformation
↓
Dataset Merging
↓
Feature Engineering
↓
Final Dataset (CSV)
↓
Power BI Dashboard

---

## Data Pipeline

The pipeline is implemented in Python and performs the following steps:

- Ingests multiple datasets from web sources  
- Cleans and standardizes inconsistent data  
- Handles duplicate and multi-team players (2TM / 3TM logic)  
- Converts salary data into numeric format  
- Filters players based on minimum playing time and games played  
- Merges datasets into a unified player-level table  

---

## Methodology

### Per-36 Normalization

All player production metrics are normalized to a per-36-minute basis to ensure fair comparisons across players with different playing time.

---

### Impact Score
Impact Score =
Per36Impact
× (0.90 + TS% × 0.25)
× (0.85 + USG% × 0.01)

OBPM × 1.5
DBPM × 1.5


This incorporates:
- Scoring, playmaking, rebounding, and defense  
- Efficiency (True Shooting %)  
- Usage rate  
- Advanced impact metrics (OBPM, DBPM)  

---

### Value Score
Value = Impact Score / √Salary
Value Score = Value × 1000


This approach prevents high-salary players from being overly penalized while still highlighting cost efficiency.

---

## Dashboard Features

The Power BI dashboard includes:

- Top Impact Players  
- Top Value Players  
- Salary vs Impact analysis  
- Impact composition (Offensive / Defensive / Negative)  
- Interactive slicers (Player, Team, Salary Tier)

---

## Key Insights

- Offensive production and efficiency drive the majority of player impact  
- Value is strongly influenced by contract structure rather than raw performance  
- Mid-tier salary players often provide the highest return on investment  

---

## Tech Stack

- Python (pandas)  
- Power BI  
- Data Modeling & Feature Engineering  

---

## Project Structure
NBA-Data-Pipeline/
├── Data/
├── Scripts/
│ └── build_pipeline.py
├── Dashboard/
├── images/
└── README.md

---

## Future Improvements

- Automate data pipeline updates  
- Integrate a database (SQL or cloud storage)  
- Expand the model with additional advanced metrics  
- Enable real-time or season-updating data  

---

## Contact

Feel free to connect or reach out via LinkedIn for feedback or collaboration.
https://www.linkedin.com/in/dillandbailey/