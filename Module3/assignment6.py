import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheat = pd.read_csv ('Datasets/wheat.data')
#print wheat.head ()

#
# TODO: Drop the 'id' feature
# 
# .. your code here ..
wheat = wheat.drop (labels = ['id'], axis = 1)

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
wheat.corr ()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow (wheat.corr(), cmap=plt.cm.Blues, inerpolation='nearest')
plt.colorbar ()
tick_marks = [i for i in range (len(wheat.columns))]
plt.xticks (tick_marks, wheat.columns, rotation='vertical')
plt.yticks (tick_marks, wheat.columns)

plt.show()