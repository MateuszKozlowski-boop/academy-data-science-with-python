# Check to see if there are any categorical features or missing values in the data.

X.dtypes


# Now check to see if there is any missing data.

X.isnull().sum()