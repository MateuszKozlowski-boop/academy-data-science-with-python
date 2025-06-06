
# 1
(
    chickweight
    .loc[lambda df: df['weight'] > 150]
)

# 2
(
    chickweight
    .loc[lambda df: df['diet'] == 4]
)

# 3
(
    chickweight
    .loc[lambda df: df['time'] == 2]
    .loc[lambda df: df['weight'] < 60]
)

# 4
(
    chickweight
    .loc[lambda df: df['weight'] < 60, ['weight', 'time']]
    .loc[lambda df: df['time'] == 2]
)

# bonus 1
(
    chickweight['weight']
    .mean()
)

# bonus 2
(
    chickweight
    .loc[lambda df: df['time'] == 10, "weight"]
    .mean()
)
