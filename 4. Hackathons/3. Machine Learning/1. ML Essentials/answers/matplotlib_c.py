# +
fig, ax = plt.subplots()

class_one.plot(kind='scatter', 
          x='alcohol',
          y='color_intensity', 
          color='r',
          ax=ax)

class_two.plot(kind='scatter', 
          x='alcohol',
          y='color_intensity', 
          color='b',
          ax=ax)

class_three.plot(kind='scatter', 
          x='alcohol',
          y='color_intensity', 
          color='g',
          ax=ax)
