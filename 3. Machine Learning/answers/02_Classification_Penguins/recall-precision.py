
from sklearn.metrics import precision_score, recall_score

precision = precision_score(y_test, y_pred, average=None)
recall = recall_score(y_test, y_pred, average=None)

pd.DataFrame({'Species':model.classes_, 'Precision': precision, 'Recall':recall}).set_index('Species')