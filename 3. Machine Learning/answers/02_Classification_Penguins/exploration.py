
# 1. How many rows and columns are present in the data?
penguins.shape

# 2. Which data types are used by each column?
penguins.dtypes
# or
penguins.info()

# 3. Are there any missing values?
penguins.isna().sum()
# or
penguins.info()

# 4. How many species are there?
penguins['species'].nunique()
# or
len(penguins['species'].unique())

# 5. How many penguins are there for each species?
penguins['species'].value_counts()