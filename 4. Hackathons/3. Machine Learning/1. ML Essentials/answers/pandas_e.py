(
    wine['class']
    .value_counts()
    .plot(kind='pie', 
          title='Pie chart showing how many wines are present from each class.')
)
