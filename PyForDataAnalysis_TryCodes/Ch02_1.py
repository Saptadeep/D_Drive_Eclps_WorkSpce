# %load D:\Eclipse_Workspace\PyForDataAnalysis\Ch02_1.py
#%matplotlib inline
#%pdb
from pandas import DataFrame, Series
import json
import numpy as np
#import pdb
#pdb.set_trace()
#path = 'D:/Eclipse_Workspace/pydata-book-master/PyForDataAnalysis_Extracted/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
path = 'D:/Eclipse_Workspace/zz1.py'
records = [json.loads(line) for line in open(path)]


frame = DataFrame(records)
frame['index'] = frame.index
#print(frame['index'])
#pdb.set_trace()
#print(frame.index)
#pdb.set_trace()
#print (len(frame))
#print (len(frame['tz']))

print ('print((frame)):')

print((frame))

clean_tz = frame['tz'].fillna('KeyItselfMissing')

print ('print (clean_tz)')
clean_tz[clean_tz == ''] = 'KeyPresent_ValueMissing'
print (clean_tz) #[clean_tz == ''] = 'Unknown')

print (frame.fillna('KeyItselfMissing'))
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones)


from matplotlib import pyplot as plt
import numpy
#x = numpy.linspace(0, 1, 1000)**1.5
#plt.hist(x);
frame['a'].value_counts().plot(kind='bar',rot=0)
results1 = ([x.split()[0] for x in frame.a.dropna()])
results2 = Series([x.split()[0] for x in frame.a.dropna()])
results1[0]
results1[1]
results1

frame['a'].value_counts().plot(kind='bar',rot=0)

