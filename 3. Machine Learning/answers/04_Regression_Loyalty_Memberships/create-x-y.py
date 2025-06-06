feature_columns = ['time on app', 'length of membership']
X = customers.loc[:, feature_columns]
y = customers.loc[:, 'yearly amount spent']