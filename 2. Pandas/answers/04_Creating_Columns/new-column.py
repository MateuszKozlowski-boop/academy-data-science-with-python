
(
    chickweight
    .assign(weight_kg = lambda df: df['weight'] / 1000,
            weight_lbs = lambda df: df['weight_kg'] * 2.205)
)
