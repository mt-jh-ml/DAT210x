import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheat = df.read_csv ('Datasets/wheat.data')
print wheat.head ()

#
# TODO: Drop the 'id' feature
# 
# .. your code here ..
#df = df.drop (labels = ['id'], axis = 1)
wheat = wheat.drop (labels = ['id'], axis = 1)

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
df.corr ()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow (df.corr (), cmap = plt.cm.Blues, inerpolation = 'nearest')
plt.colorbar ()
tick_marks = [i for i in range (len(df.columns))]
plt.xticks (tack_marks, df.columns, rotation = 'vertical')
plt.yticks (tack_marks, df.columns)

plt.show()


