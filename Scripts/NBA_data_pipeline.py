import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"
DATA_DIR.mkdir(exist_ok=True)

PER_GAME_URL = "https://www.basketball-reference.com/leagues/NBA_2026_per_game.html"
ADVANCED_URL = "https://www.basketball-reference.com/leagues/NBA_2026_advanced.html"
SALARY_URL = "https://www.basketball-reference.com/contracts/players.html"


def read_bref_table(url):
    df = pd.read_html(url)[0]
    df = df[df["Player"] != "Player"]
    return df


def clean_money(value):
    if pd.isna(value):
        return 0

    return (
        str(value)
        .replace("$", "")
        .replace(",", "")
        .replace("-", "0")
    )


# -----------------------------
# 1. INGEST DATA
# -----------------------------

per_game = read_bref_table(PER_GAME_URL)
advanced = read_bref_table(ADVANCED_URL)
salary = pd.read_html(SALARY_URL, header=1)[0]

# Flatten salary columns if needed
if isinstance(salary.columns, pd.MultiIndex):
    salary.columns = salary.columns.get_level_values(0)

# Save raw datasets
per_game.to_csv(DATA_DIR / "raw_per_game.csv", index=False)
advanced.to_csv(DATA_DIR / "raw_advanced.csv", index=False)
salary.to_csv(DATA_DIR / "raw_salary.csv", index=False)


# -----------------------------
# 2. CLEAN PER-GAME DATA
# -----------------------------

per_game = per_game.rename(columns={"Tm": "Team"})

per_game_cols = [
    "Player", "Team", "Pos", "G", "MP",
    "PTS", "AST", "ORB", "DRB", "TRB",
    "STL", "BLK", "TOV", "PF",
    "FG%", "3P", "3PA", "3P%", "eFG%"
]

per_game = per_game[per_game_cols]

per_game_numeric_cols = [
    "G", "MP", "PTS", "AST", "ORB", "DRB", "TRB",
    "STL", "BLK", "TOV", "PF",
    "FG%", "3P", "3PA", "3P%", "eFG%"
]

for col in per_game_numeric_cols:
    per_game[col] = pd.to_numeric(per_game[col], errors="coerce")

per_game = per_game.fillna(0)


# -----------------------------
# 3. CLEAN ADVANCED DATA
# -----------------------------

advanced = advanced.rename(columns={"Tm": "Team"})

advanced_cols = [
    "Player", "Team",
    "PER", "TS%", "USG%", "OBPM", "DBPM", "BPM", "VORP"
]

advanced = advanced[advanced_cols]

advanced_numeric_cols = ["PER", "TS%", "USG%", "OBPM", "DBPM", "BPM", "VORP"]

for col in advanced_numeric_cols:
    advanced[col] = pd.to_numeric(advanced[col], errors="coerce")

advanced = advanced.fillna(0)


# -----------------------------
# 4. CLEAN SALARY DATA
# -----------------------------

salary = salary[salary["Player"] != "Player"]

salary_col = "2025-26"

salary = salary[["Player", salary_col]]
salary = salary.rename(columns={salary_col: "Salary"})

salary["Salary"] = salary["Salary"].apply(clean_money)
salary["Salary"] = pd.to_numeric(salary["Salary"], errors="coerce").fillna(0)


# -----------------------------
# 5. MERGE DATASETS
# -----------------------------

df = per_game.merge(
    advanced,
    on=["Player", "Team"],
    how="left"
)

df = df.merge(
    salary,
    on="Player",
    how="left"
)

df["Salary"] = df["Salary"].fillna(0)


# -----------------------------
# 6. ELIGIBILITY FILTER
# -----------------------------

df = df[(df["MP"] >= 10) & (df["G"] >= 20)]
df = df[df["Salary"] > 0]


# -----------------------------
# 7. PER-36 TRANSFORMATIONS
# -----------------------------

df["PTS_36"] = df["PTS"] / df["MP"] * 36
df["AST_36"] = df["AST"] / df["MP"] * 36
df["DRB_36"] = df["DRB"] / df["MP"] * 36
df["ORB_36"] = df["ORB"] / df["MP"] * 36
df["STL_36"] = df["STL"] / df["MP"] * 36
df["BLK_36"] = df["BLK"] / df["MP"] * 36
df["TOV_36"] = df["TOV"] / df["MP"] * 36
df["PF_36"] = df["PF"] / df["MP"] * 36


# -----------------------------
# 8. PER-36 IMPACT MODEL
# -----------------------------

df["Per36Impact"] = ****


# -----------------------------
# 9. IMPACT SCORE
# Matches Power BI:
# Per36Impact
# * (0.90 + TS% * 0.25)
# * (0.85 + USG% * 0.01)
# + OBPM * 1.5
# + DBPM * 1.5
# -----------------------------

df["Impact_Score"] = ****
)


# -----------------------------
# 10. HANDLE 2TM / 3TM ROWS
# Prefer combined team rows when available
# -----------------------------

df["Is_Combined_Team_Row"] = df["Team"].isin(["2TM", "3TM"])

df = (
    df.sort_values(
        ["Player", "Is_Combined_Team_Row"],
        ascending=[True, False]
    )
    .drop_duplicates(subset=["Player"], keep="first")
)


# -----------------------------
# 11. VALUE SCORE
# Matches Power BI:
# Value = Impact Score / SQRT(Player Salary)
# Value Score = Value * 1000
# -----------------------------

df["Value"] = df.apply(
    lambda row: row["Impact_Score"] / (row["Salary"] ** 0.5)
    if row["Salary"] > 0 else 0,
    axis=1
)

df["Value_Score"] = df["Value"] * 1000


# -----------------------------
# 12. RANKS
# -----------------------------

df["Impact_Rank"] = df["Impact_Score"].rank(ascending=False)
df["Value_Rank"] = df["Value_Score"].rank(ascending=False)

df = df.sort_values("Impact_Rank")


# -----------------------------
# 13. SAVE FINAL DATASET
# -----------------------------

final_file = DATA_DIR / "clean_nba_player_impact_value.csv"
df.to_csv(final_file, index=False)

print("Pipeline completed successfully")
print(f"Rows in final dataset: {len(df)}")
print(f"Saved to: {final_file}")
