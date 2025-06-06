# Split the data into X and y where X is the feature matrix and y is the target (class)

features = [
    'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium',
    'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
    'proanthocyanins', 'color_intensity', 'hue',
    'od280/od315_of_diluted_wines', 'proline'
]

X = wine.loc[:, features]
y = wine.loc[:, 'class']


# Check the shape of X and y. 

X.shape, y.shape


# Perform a value_counts() on y to see how many classes of 0, 1, 2 there are. Use normalize=True to see this as a percentage.

y.value_counts(normalize=True)