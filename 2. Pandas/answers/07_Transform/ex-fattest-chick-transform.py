(
    pd.merge(
        chickweight,
        chickweight.groupby('diet')['weight'].transform('max').rename('max_weight'),
        left_index=True,
        right_index=True
    )
    .loc[lambda df: df['weight']==df['max_weight']]
)