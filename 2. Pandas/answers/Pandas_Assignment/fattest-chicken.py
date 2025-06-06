(
    chickweight
    .sort_values('weight')
    .groupby('diet')
    .last()
)
