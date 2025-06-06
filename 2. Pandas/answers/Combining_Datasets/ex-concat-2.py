pd.concat([diet_1, diet_2], axis=1)

print(f"There are {diet_1.shape[0]} rows in diet_1 and {diet_2.shape[0]} in diet_2")

# Due to the mis-match of the number of rows, there are no values past row 220 
# for diet_2