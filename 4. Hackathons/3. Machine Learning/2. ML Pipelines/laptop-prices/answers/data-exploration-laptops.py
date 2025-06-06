
# 1. What are the data types of each column?

laptops.dtypes


# 2. What is the average price of a laptop when split by (groupby) company? Bonus: Plot this as a horizontal bar plot.

(
    laptops
    .groupby('company')
    ['price']
    .mean()
    # bonus
    .sort_values()
    .plot(kind='barh', figsize=(10,6))
)


# 3. Use groupby to find the mean weight of a laptop split by (groupby) the operating system.

(
    laptops
    .groupby('op_sys')['weight']
    .mean()
    # bonus
    .sort_values()
    .plot(kind='barh', figsize=(10,6))
)


# 4. How many unique values are there in each categorical variable? 

laptops.select_dtypes('object').nunique()
# want to exclude features with lots of unique values as the amount 
# of observations for each category would be small

# 5. Show for each type of laptop which company produces the most
(
    laptops.groupby(['company', 'type_name']).size()
    # bonus
    .unstack()
    .idxmax()
)
