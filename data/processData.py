import pandas as pd

sheet_id = "1CrADExohsLWq7vGZhaonv0nHoEUQfKkVnnjnETOM3Os"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

# Raw data
trees = pd.read_csv(url)

# Dropping unnecessary columns
trees = trees.drop(columns=[
    "title",
    "ec5_uuid",
    "created_at",
    "uploaded_at",
    "1_Surveyor_Name",
    "accuracy_2_Location",
    "5_Photo",
    "UTM_Northing_2_Location",
    "UTM_Easting_2_Location",
    "UTM_Zone_2_Location"
])

# Renaming columns so that it is easier to read/work with
trees = trees.rename(columns={"lat_2_Location": "Latitude",
                      "long_2_Location": "Longitude",
                      "3_Park_Location": "Site",
                      "4_Tree_ID": "Tree ID",
                      "6_Diameter_at_Breast": "DBH",
                      "7_Tree_Height_ft": "Tree Height",
                      "8_Tree_Spread_tip_to": "Spread 1",
                      "9_Tree_Spread_tip_to": "Spread 2",
                      "10_Tree_Condition": "Tree Condition",
                      "11_Notes_eg_mushroom": "Notes"})

"""
In the data collection process, if the tree is either
a young or newly planted tree, it is specified in the notes. 
It is also specified if the tree is multi-branch or not. 

Here, we create new columns that specified the type of significant tree
and if the tree is a multi-branch.
"""
for i, tree in trees.iterrows():
    note = str(tree["Notes"]).lower()

    if ("new" in note) or ("cage" in note):
        trees.loc[i, "Type of Significant Trees"] = "Newly planted tree"
    elif "young tree" in note:
        trees.loc[i, "Type of Significant Trees"] = "Young tree"
    else:
        trees.loc[i, "Type of Significant Trees"] = "Large mature tree"

    if ("diverge" in note) or ("multi branch" in note):
        trees.loc[i, "Multi-branch?"] = "Yes"
    else:
        trees.loc[i, "Multi-branch?"] = "No"

# Compute average spread and store it in a column
trees["Average Spread"] = trees[["Spread 1", "Spread 2"]].mean(axis=1)

# Save the DataFrame to a CSV file
trees.to_csv("processedTreeData.csv", index=False)