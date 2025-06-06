(
    chickweight
    .assign(diff = lambda df: df.groupby('chick')['weight'].diff())
    .fillna(0)
    .groupby(['time'])
    .agg(mean_weight_increase=('diff', 'mean'))
    ['mean_weight_increase']
    .plot(title='Average Growth over Time', ylabel='Growth')
);

