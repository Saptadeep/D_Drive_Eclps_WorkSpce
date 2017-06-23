%config InlineBackend.figure_format = 'retina'
#Pp68_ISLR_CollegeDataExplore
from IPython.display import display, Image
import pandas as pd
import matplotlib as mplt
import matplotlib.pyplot as plt

from pandas.tools.plotting import scatter_matrix

p_df = pd.read_csv("College.csv")

scatter_matrix(p_df.iloc[:,:10], alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.savefig('sctr23Jun.png')
display(Image('sctr23Jun.png'))

plt.show()