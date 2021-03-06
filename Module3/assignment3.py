import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheat = pd.read_csv ('Datasets/wheat.data')
print wheat.head (6)


fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..
ax1 = fig.add_subplot (111, projection = '3d')
ax1.set_xlabel ('area')
ax1.set_ylabel ('perimeter')
ax1.set_zlabel ('asymmetry')
ax1.scatter (wheat ['area'], wheat ['perimeter'], wheat ['asymmetry'], c = 'red', marker = '.')

fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..
ax2 = fig.add_subplot (111, projection = '3d')
ax2.set_xlabel ('width')
ax2.set_ylabel ('groove')
ax2.set_zlabel ('length')
ax2.scatter (wheat ['width'], wheat ['groove'], wheat ['length'], c = 'green', marker = '.')

plt.show()


