# How many (unique customers):
customers['email'].nunique()

# Dtypes
customers.dtypes

# Missing values
customers.isnull().sum()

# Which features could be predictive?
customers.info() 