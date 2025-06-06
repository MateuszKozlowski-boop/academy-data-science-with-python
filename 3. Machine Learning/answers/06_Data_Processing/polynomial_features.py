from sklearn.preprocessing import PolynomialFeatures

pipeline = Pipeline(steps=[
    ('onehot', column_transformer), 
    ('poly_features', PolynomialFeatures()),
    ('scaler', MinMaxScaler()),
    ('model', SVC())
])

pipeline.fit(X_train, y_train)

y_hat = pipeline.predict(X_test)
accuracy_score(y_test, y_hat)