print(f'Train set accuracy:', pipeline_knn.score(X_train, y_train))
print(f'Test set accuracy:', pipeline_knn.score(X_test, y_test))