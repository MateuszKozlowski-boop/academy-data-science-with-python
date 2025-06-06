
# Predict y on test data
y_pred = model.predict(X_test)

# Let's compare to actual values
np.array([y_test[:10], y_pred[:10]]).T