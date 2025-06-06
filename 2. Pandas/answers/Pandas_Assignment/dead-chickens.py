(
    chickweight
    .groupby('chick')
    .max()
    .loc[lambda df: df['time'] < df['time'].max()]
)
