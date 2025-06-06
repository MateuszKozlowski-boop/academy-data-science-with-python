# option 1: reset_index
pd.concat([diet_1, diet_2, diet_3, diet_4]).reset_index(drop=True)

# option 2: parameter
pd.concat([diet_1, diet_2, diet_3, diet_4], ignore_index=True)