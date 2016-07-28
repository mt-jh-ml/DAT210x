import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
csv = pd.read_csv ('/home/chiku/DAT210x/tutorial.csv')
print (csv)

# TODO: Print the results of the .describe() method
#
# .. your code here ..
print ('Describe tutorial.csv')
print (csv.describe())

# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print ('Column 3 of rows 2 and 3')
print (csv.loc[2:4,'col3'])