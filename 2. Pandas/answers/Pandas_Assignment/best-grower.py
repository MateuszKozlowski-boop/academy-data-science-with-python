(
    chickweight
    .groupby(['chick', 'diet'])
    ['weight']
    .agg(['first', 'last'])
    .assign(growth_rate = lambda df: df['last'].div(df['first']).round(2))
    .sort_values('growth_rate', ascending=False)
)