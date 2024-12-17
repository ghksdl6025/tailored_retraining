import pandas as pd
import numpy as np
import os, sys
from collections import Counter

log_list = [x for x in os.listdir('./DATA/logs/') if 'csv' in x]
ds_dict = {}

for log in log_list:
    variant_set = set()
    true_label = 0
    false_label = 0
    log_path = './DATA/logs/%s'%(log)
    df= pd.read_csv(log_path)
    log = log[:-4]
    df['Complete Timestamp'] = pd.to_datetime(df['Complete Timestamp'])

    activity_list = set(list(df['Activity']))
    
    groups = df.groupby('Case ID')
    lengths = []
    ds_dict[log] = {}
    for _, group in groups:
        lengths.append(len(group))
        group = group.sort_values(by='Complete Timestamp')
        variant = ''
        for x in list(group['Activity']):
            variant += x
        variant_set.add(variant)
        outcome = set(list(group['outcome']))
        if True in outcome:
            true_label +=1
        elif False in outcome:
            false_label += 1

    ds_dict[log]['# cases'] =len(groups)
    ds_dict[log]['# events'] =len(df)
    ds_dict[log]['# activities'] =len(activity_list)
    ds_dict[log]['# variant'] =len(variant_set)
    ds_dict[log]['Mean'] = round(np.mean(lengths),1)
    ds_dict[log]['Median'] = round(np.median(lengths),1)
    ds_dict[log]['# true labels'] = true_label
    ds_dict[log]['# false labels'] = false_label

dft = pd.DataFrame.from_dict(ds_dict).T
dft.to_csv('./descriptive_statistics.csv')
print(dft.head)