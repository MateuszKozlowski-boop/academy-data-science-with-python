# 1 
(
    chickweight
    .loc[lambda df: (df['weight'] > 50) & (df['weight'] < 100)]
)
# or:
(
    chickweight
    .loc[lambda df: df['weight'].between(50, 100, inclusive = "neither")]
)

# 2
(
    chickweight
    .loc[lambda df: (df['diet'] == 1) | (df['diet'] == 2)]
)

# or:
(
    chickweight
    .loc[lambda df: df['diet'].isin([1, 2])]
)

# 3

(
    chickweight
    .loc[lambda df: (df['weight'] < 60) & (df['time'] == 2), ['weight', 'time']]
)
