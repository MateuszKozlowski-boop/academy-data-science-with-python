
from sklearn import metrics

print('MAE:', round(metrics.mean_absolute_error(y_test, y_pred), 4))
print('MSE:', round(metrics.mean_squared_error(y_test, y_pred), 4))
print('RMSE:', round(metrics.root_mean_squared_error(y_test, y_pred), 4))