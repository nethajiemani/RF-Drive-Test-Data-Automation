import pandas as pd

# 1. Load your raw drive test log
df = pd.read_csv("drive_test_data.csv")

# 2. Filter for BOTH weak RSRP (< -100) AND poor SINR (< 5) using '&'
trouble_spots = df[(df["RSRP"] < -100) & (df["SINR"] < 5)]

print(f"Found {len(trouble_spots)} severe trouble spots needing optimization.")

# 3. Automatically export those trouble spots to a brand new CSV report
trouble_spots.to_csv("weak_coverage_report.csv", index=False)

print("Report successfully saved as 'weak_coverage_report.csv'!")