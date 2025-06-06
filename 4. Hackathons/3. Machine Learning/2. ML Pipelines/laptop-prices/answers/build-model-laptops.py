from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

model_lr = LinearRegression()

pipeline_lr = Pipeline(steps = [
    ('onehot', column_transformer),
    ('scaler', StandardScaler()),
    ('model', model_lr)
])


# Fit the pipeline to X_train and y_train

pipeline_lr.fit(X_train, y_train)