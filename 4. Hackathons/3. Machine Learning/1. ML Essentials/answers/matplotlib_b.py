# +
fig, (left, center, right) = plt.subplots(1,3, figsize=(12,4))

left.plot(class_one['alcohol'], class_one['color_intensity'], 'ro')
center.plot(class_two['alcohol'], class_two['color_intensity'], 'bo')
right.plot(class_three['alcohol'], class_three['color_intensity'], 'go')

fig.tight_layout()

