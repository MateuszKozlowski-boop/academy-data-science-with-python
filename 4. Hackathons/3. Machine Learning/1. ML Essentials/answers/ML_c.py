from sklearn.tree import plot_tree

labels = ['class 0', 'class 1', 'class 2']

fig, ax = plt.subplots(figsize=(14,10))

plot_tree(model, ax=ax, feature_names = X.columns, class_names=labels);