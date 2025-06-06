(
    chickweight
    .assign(difference = lambda x: x.groupby('chick')['weight'].diff())
    .fillna(0)
)

