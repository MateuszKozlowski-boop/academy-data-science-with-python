column_transformer = ColumnTransformer([
    ('onehot_encoder', OneHotEncoder(sparse_output=False), categorical_columns)
    ], remainder="passthrough")

X_encoded = column_transformer.fit_transform(X_train)

print(column_transformer.named_transformers_['onehot_encoder'].get_feature_names_out())
# for older versions of sklearn:
# print(column_transformer.named_transformers_['onehot_encoder'].get_feature_names())

X_encoded.shape