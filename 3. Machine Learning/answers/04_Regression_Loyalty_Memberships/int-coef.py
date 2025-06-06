# Print the intercept
print("Intercept", model.intercept_)

# Print the coefficients
coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)