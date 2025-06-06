
# Exercise 1 and 3
(
    chickweight
    .assign(differences = lambda df: df.groupby('chick')['weight'].diff())
)

# Exercise 4
(
    chickweight
    .assign(differences = lambda df: df.groupby('chick')['weight'].diff())
#   .dropna()
    .fillna(0)
)