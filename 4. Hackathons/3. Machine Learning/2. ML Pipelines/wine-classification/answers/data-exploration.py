# 1. What are the data types of each column?

wine.dtypes


# 2. Use .value_counts() to find out how many of each type of wine you have

wine['class'].value_counts()


# 3. Use groupby to find the mean value for all the features when split (groupby) the class of wine

wine.groupby('class').mean()


# Part 4 & 5 left as an exercise to the reader
