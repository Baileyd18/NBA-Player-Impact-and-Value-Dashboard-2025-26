# NBA-Player-Impact-and-Value-Dashboard-2025-26
Power BI dashboard analyzing 2025–26 NBA player performance using a custom efficiency-adjusted impact model. Combines box score metrics and salary data sourced directly from Basketball Reference to evaluate player performance, contract value, and league-wide trends through interactive visualizations.

---
## Link to Dashboard

https://app.powerbi.com/view?r=eyJrIjoiZGUzYTljMjYtZmQyNC00OTc4LTkxMGQtZTlmYzY3NzU0YWQ4IiwidCI6ImFjMjRjMTRiLTc3YTEtNDZmYy1hOTY5LTkwNDRiYTIzMTc0MyJ9&embedImagePlaceholder=true
---

## Data Sources

Data was compiled from Basketball Reference:

- Per-game player statistics:  
  https://www.basketball-reference.com/leagues/NBA_2026_per_game.html

- Player salary data:  
  https://www.basketball-reference.com/contracts/players.html

These datasets were merged to create a unified player-level dataset for the 2025–26 NBA season.

---

## Data Preparation

Data was cleaned and transformed using Power Query:

- Standardized column names and data types  
- Merged statistical and salary datasets  
- Handled traded players using `2TM / 3TM` rows to avoid duplication  
- Removed duplicates and unnecessary fields  
- Filtered players with:
  - ≥10 Minutes Per Game  
  - ≥20 Games Played  

---

## Feature Engineering

### Total Impact

A weighted combination of per-36 box score statistics:

- Points  
- Assists
- Offensive and defensive rebounds  
- Steals and blocks (positively weighted)  
- Turnovers and fouls (penalized)  

### Impact Score

Adjusts Total Impact using shooting efficiency:

- Based on eFG%  
- Rewards efficient scoring alongside volume production  

### Value Score

Evaluates performance relative to salary:

- Uses a non-linear salary penalty to reduce over-penalization of high-salary players  
- Highlights cost-efficient contributors  

### Player Ranking

- Built using DAX `RANKX`  
- Ranks players across the filtered NBA population  
- Updates dynamically based on filters  

---

## Dashboard Features

### KPI Cards

- Average Salary  
- Average Impact  
- Players Analyzed  
- Top Impact Player  
- Top Value Player  
- Player Rank  

---

## Visualizations

### Impact vs Salary (Scatter Plot)

Shows the relationship between player cost and performance, including a trendline for expected value.

### Top Contract Values (Bar Chart)

Highlights players delivering the highest value relative to salary.

### Impact Composition by Player (100% Stacked Bar Chart)

Displays how each player’s total impact is distributed across key components, with tooltips for:

- Scoring Impact %
- Playmaking Impact %
- Rebounding Impact %
- Defensive Impact %
- Efficiency Impact %
- Usage Impact %
- Negative Impact %
- Impact Score
- Value Score

---

## Interactivity

The dashboard includes filters for:

- Player  
- Team  
- Position  
- Salary Tier  
- Minutes Per Game  

These enable both league-wide analysis and focused player or team exploration.

---

## Tools Used

- Power BI  
- DAX (Data Analysis Expressions)  
- Power Query  
- Microsoft Excel  
- Basketball Reference  

---

## How to Use

1. Apply filters to explore specific players, teams, or salary tiers  
2. Analyze performance using Impact and Value metrics  
3. Compare contract efficiency across the league  
4. Identify high-value players and potential inefficiencies  

---

## Notes

- Includes players with ≥10 MPG and ≥20 games played  
- Accounts for traded players using combined rows (`2TM`, `3TM`)  
- Designed for analytical exploration, not predictive modeling  
