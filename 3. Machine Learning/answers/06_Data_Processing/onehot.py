onehot_encoder = OneHotEncoder(sparse_output=False)
# Fit the encoder. 
onehot_encoder.fit(X_train[categorical_columns])
# Transform the data.
encoded_columns = onehot_encoder.transform(X_train[categorical_columns])

print(f'Shape before transformation {X_train[categorical_columns].shape}, shape after transformation {encoded_columns.shape}.')

print(f'New feature names {onehot_encoder.get_feature_names_out()}')
# if you have an older version of sklearn, the method above might not work. In that case try:
# print(f'New feature names {onehot_encoder.get_feature_names()}')

encoded_columns