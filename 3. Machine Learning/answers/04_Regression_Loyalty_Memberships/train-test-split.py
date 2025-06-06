from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100, test_size=0.3)
print(f'X_train shape: {X_train.shape}', 
      f'X_test shape: {X_test.shape}', 
      f'y_train shape: {y_train.shape}', 
      f'X_test shape: {y_test.shape}',
     sep='\n')