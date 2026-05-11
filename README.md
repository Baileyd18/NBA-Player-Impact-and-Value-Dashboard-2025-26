# NBA Player Impact & Value Analytics Pipeline

## Live Dashboard
[Interactive Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiODA1MjVkODUtNGE3Zi00MmIwLTljYjUtMmQ2ZmFjNDMxM2E4IiwidCI6ImFjMjRjMTRiLTc3YTEtNDZmYy1hOTY5LTkwNDRiYTIzMTc0MyJ9)

---

## Overview

This project builds an end-to-end automated analytics pipeline that transforms raw NBA data into a structured business intelligence dataset used to evaluate player performance and contract efficiency.

Originally developed as a Power BI dashboard focused on player value analysis, the project evolved into a broader workflow automation and reporting optimization initiative using Python, Azure, and Power BI.

The platform automates data ingestion, transformation, validation, cloud storage, and KPI-driven reporting workflows to support scalable and repeatable analytics processes.

---

## Business Problem

Traditional NBA statistics such as points, rebounds, and assists do not fully capture a player’s total impact or value relative to salary investment.

Additionally, manual reporting workflows created several operational inefficiencies:
- repetitive manual data preparation
- inconsistent dashboard refreshes
- duplicate/traded-player handling challenges
- fragmented reporting processes
- scalability limitations
- increased risk of human error

This project addressed both analytical and operational challenges by redesigning the workflow into an automated cloud-integrated analytics pipeline.

---

## Data Sources

Data was collected from Basketball Reference:
- Per-game player statistics
- Advanced player statistics
- Player salary data

---

## Automated Pipeline Architecture

Basketball Reference  
↓  
Python ETL Pipeline  
↓  
Automated Cleaning & Transformation  
↓  
Duplicate / Multi-Team Player Handling  
↓  
Feature Engineering  
↓  
Processed CSV Dataset  
↓  
Azure Blob Storage  
↓  
Azure Data Factory Orchestration  
↓  
Power BI Dataset Refresh  
↓  
Power BI Dashboard  

---

## Automated Data Pipeline

The pipeline is implemented in Python and performs the following operations:

- ingests multiple datasets from web sources
- standardizes inconsistent schemas
- handles duplicate and traded-player rows (2TM / 3TM logic)
- converts salary data into numeric format
- filters players based on minimum games played and playing time
- validates transformed datasets
- merges datasets into a unified player-level table
- exports processed datasets into cloud storage
- orchestrates automated refresh workflows through Azure Data Factory
- updates KPI-driven Power BI reporting dashboards

---

## Workflow Automation

To improve scalability and reduce operational dependency on manual refreshes, the reporting workflow was redesigned into an automated cloud-integrated process.

### Automation Improvements
- automated ETL processing
- standardized transformation workflows
- centralized cloud-based dataset storage
- automated dataset refresh orchestration
- repeatable analytics reporting lifecycle
- improved reporting consistency and reliability

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

+ (OBPM × 1.5)  
+ (DBPM × 1.5)

This incorporates:
- scoring, playmaking, rebounding, and defense
- efficiency (True Shooting %)
- usage rate
- advanced impact metrics (OBPM, DBPM)

---

### Value Score

Value = Impact Score / √Salary  
Value Score = Value × 1000

This approach prevents high-salary players from being overly penalized while still highlighting contract efficiency.

---

## Dashboard Features

The Power BI dashboard includes:
- Top Impact Players
- Top Value Players
- Salary vs Impact analysis
- Impact composition analysis
- Interactive slicers and filters
- KPI-driven player evaluation
- Automated reporting refresh workflows

---

## Key Insights

- offensive production and efficiency drive the majority of player impact
- value is heavily influenced by contract structure
- mid-tier salary players often generate the highest return on investment
- automation significantly improved reporting consistency and workflow efficiency
- centralized cloud storage improved scalability and repeatability

---

## Technical Challenges & Solutions

| Challenge | Solution |
|---|---|
| Duplicate traded-player records | Combined-row transformation logic |
| Manual dashboard refresh dependency | Automated reporting workflows |
| Dataset inconsistencies | Schema standardization |
| Workflow orchestration | Azure Data Factory automation |
| Validation accuracy | Data quality checkpoints |

---

## Tech Stack

### Business Intelligence
- Power BI
- DAX
- Power Query

### Automation & ETL
- Python
- pandas
- ETL workflows

### Cloud & Orchestration
- Azure Blob Storage
- Azure Data Factory

---

## Project Structure

NBA-Data-Pipeline/  
├── Data/  
├── Scripts/  
│   └── build_pipeline.py  
├── Dashboard/  
├── images/  
└── README.md  
