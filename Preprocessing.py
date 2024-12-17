import pandas as pd
import datetime

df = pd.read_csv('./DATA/logs/outcome_oriented/BPIC17_O_Refused.csv', sep=';')
print(df.columns.values)
df = df.loc[:,['Case ID', 'Activity', 'org:resource', 'time:timestamp', 'label']]
df = df.rename(columns={'label':'outcome', 'org:resource': 'Resource','time:timestamp':'Complete Timestamp'})
df['Complete Timestamp'] = pd.to_datetime(df['Complete Timestamp'])

print(df)

# df['Start Timestamp'] = pd.to_datetime(df['Start Timestamp'])

groups = df.groupby('Case ID')

concating = []
count =0
for _, group in groups:
    group = group.reset_index(drop=True)
    group = group.sort_values(by='Complete Timestamp')


    label = list(group['outcome'])[0]
    group = group.drop(columns=['outcome'])
    last_event = len(group)
    group.loc[last_event, 'Case ID'] = list(group['Case ID'])[0]
    group.loc[last_event, 'Activity'] = 'Release'
    group.loc[last_event, 'Complete Timestamp'] = list(group['Complete Timestamp'])[last_event-1] + datetime.timedelta(seconds=60)

    if label =='deviant':
        group.loc[last_event, 'outcome'] = True
    else:
        group.loc[last_event, 'outcome'] = False

# #     act1_check = False
# #     for pos, i in enumerate(list(qty_rejected)):
# #         if act1_check == False and i >0:
# #             act1_check=True
# #             outcome_idx = pos

# #     if act1_check == True:
# #         group.loc[outcome_idx:, 'outcome'] = True
# #     else:
# #         group.loc[len(group)-1, 'outcome'] = False

    concating.append(group)
    count +=1

    if count == 2000:
        break
dfs = pd.concat(concating)
dfs = dfs.sort_values(by='Complete Timestamp')

print(dfs)
print(len(set(dfs['Case ID'])))
# # dfs = dfs.loc[:, ['Case ID', 'Activity', 'Resource', 'Start Timestamp', 'Complete Timestamp', 'outcome']]
dfs.to_csv('./DATA/logs/bpic2017_3.csv', index=False)

