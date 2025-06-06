
print('List of unique values:', chickweight['time'].unique())
# Since chickens have a short lifespan, time probably represents number of days

# To count up these unique values, we can use the length function len():
print('Length of this list:', len(chickweight['time'].unique()))

# or (better) we use the build-in .nunique() method for Pandas dataframes:
print('Or with .nunique() method:', chickweight['time'].nunique())