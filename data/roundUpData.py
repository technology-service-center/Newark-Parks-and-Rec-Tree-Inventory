import pandas as pd
import numpy as np

sheet_id = "1CrADExohsLWq7vGZhaonv0nHoEUQfKkVnnjnETOM3Os"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

# Raw data
trees = pd.read_csv(url)

cols = [
    "6_Diameter_at_Breast",
    "7_Tree_Height_ft",
    "8_Tree_Spread_tip_to",
    "9_Tree_Spread_tip_to"
]

trees[cols] = np.ceil(trees[cols]).astype(int)

# Save the DataFrame to a CSV file
trees.to_csv("roundUpData.csv", index=False)