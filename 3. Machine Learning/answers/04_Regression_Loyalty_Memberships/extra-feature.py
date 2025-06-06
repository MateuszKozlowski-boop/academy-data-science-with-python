
# New feature matrix
feature_columns = ['time on app', 'length of membership', 'avg. session length']
X = customers[feature_columns]

# New train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100, train_size=0.3)
print(f'X_train shape: {X_train.shape}', 
      f'X_test shape: {X_test.shape}', 
      f'y_train shape: {y_train.shape}', 
      f'X_test shape: {y_test.shape}',
     sep='\n')

# Fitting the new model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the test values and (also the train values to see if we are over- or underfitting)
y_pred = model.predict(X_test)
train_pred = model.predict(X_train)

print('\nFit metrics on training data:')
print('MAE:', round(metrics.mean_absolute_error(y_train, train_pred),4))
print('MSE:', round(metrics.mean_squared_error(y_train, train_pred),4))
print('RMSE:', round(np.sqrt(metrics.mean_squared_error(y_train, train_pred)),4))

print('\nFit metrics on test data:')
print('MAE:', round(metrics.mean_absolute_error(y_test, y_pred),4))
print('MSE:', round(metrics.mean_squared_error(y_test, y_pred),4))
print('RMSE:', round(np.sqrt(metrics.mean_squared_error(y_test, y_pred)),4))

# Train error < Test error
# We are now slightly overfitting with the new variable.
# However, the model fit in general is much better!    