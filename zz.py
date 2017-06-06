%matplotlib inline
import pandas as pd
import matplotlib
from pandas import DataFrame, Series
import json
path = 'D:/Eclipse_Workspace/pydata-book-master/PyForDataAnalysis_Extracted/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]
df = DataFrame(records)
records[13]
tz_Counts=df['tz'].value_counts()
tz_Counts[:100]
