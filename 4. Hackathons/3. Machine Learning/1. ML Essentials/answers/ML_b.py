from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Uncomment the model that you want to try
model = DecisionTreeClassifier()
#model = RandomForestClassifier(n_estimators=1000)
# model = SVC()
#model = KNeighborsClassifier()

from sklearn.metrics import accuracy_score, classification_report
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f'Model accuracy: {model.score(X_test, y_test)}')