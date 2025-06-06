from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

model_knn = KNeighborsClassifier(n_neighbors=3)

pipeline_knn = Pipeline(steps = [
    ('scaler', StandardScaler()),
    ('model', model_knn)
])


# Fit the pipeline to X_train and y_train

pipeline_knn.fit(X_train, y_train)