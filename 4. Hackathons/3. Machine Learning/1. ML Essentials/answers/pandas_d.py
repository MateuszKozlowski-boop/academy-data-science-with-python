(
    wine['class']
    .value_counts()
    .plot(kind='bar', xlabel='cultivator', ylabel='number of wines', 
          title='Bar chart showing how many wines are present from each class.')
)
