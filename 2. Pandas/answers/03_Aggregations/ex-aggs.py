(
    chickweight
    .groupby('time')
    .agg(max_chick_id = ('chick', 'max'),
         weight_median = ('weight', 'median'),
         weight_std = ('weight', 'std'),
        )
    .loc[lambda df: df['weight_median'] > 150]
)