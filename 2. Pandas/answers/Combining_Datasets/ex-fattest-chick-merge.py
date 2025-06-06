chick_by_diet = (
    chickweight
    .groupby('diet')
    .agg(max_weight = ('weight', 'max')
        )
)

(
    pd.merge(
        chickweight,
        chick_by_diet,
        how='left',
        on='diet'
    )
    .loc[lambda df: df['weight']==df['max_weight']]
)