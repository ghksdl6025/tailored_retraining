import gzip
import pickle
import os
import pandas as pd
# log_list = [i for i in os.listdir('./result/')]
# print(log_list)
update_freq = {}
log_list = ['bpic2015_4']
classifier = 'hatc'
retraining_trigger = 'label'
for log in log_list:
    model_dir = './result/%s/%s/Finished cases/Trigger %s/'%(log, classifier, retraining_trigger)
    file_list = os.listdir(model_dir)
    model_list = [i for i in file_list if 'model'in i]
    # with open(model_dir, 'rb') as f:
    #     data = pickle.load(f)

    for model in model_list:
        with gzip.open(model_dir+model, 'rb') as f_in:
            data = pickle.load(f_in)
        update = list(data.keys())
        # print(update)
        config = log +' '+ model
        print(config, len(data.keys())-1)
        update_freq[config] = len(data.keys())-1
# print(update_freq)
