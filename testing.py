import pandas as pd
dict_schedule = {
    0 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']), 
    } 
schedule = pd.DataFrame(dict_schedule)

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714, 1], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
}
stats = pd.DataFrame(dict_stats)
stats['avg']['sum'] = stats.transpose().product().sum()

next_week = pd.Series([0,0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])
max_cap = 30000
avg_pday = max_cap / stats['avg']['sum']

def prepare(sl_intake):
    return sl_intake*stats['f']*stats['avg']


intake = pd.Series([180,70,50,40,50])
for day, animals in enumerate(intake): 
    init = prepare(animals) + schedule[(day+1)%5]
    leftover = prepare(max((init['sum']-max_cap),0)/stats['avg']['sum'])
    prepared = init - leftover - schedule[(day+1)%5]
    print("prepared on day" + str(day))
    print(prepared)
    print("leftover on day" + str(day))
    print(leftover)
    if(day+1 <= 4):
        schedule[day+1] += prepared
    else: next_week += prepared
    if(day+2 <= 4):
        schedule[day+2] += leftover
    else: next_week += leftover
    
schedule.rename(columns={0: 'Mon', 1: 'Tue', 2: 'Wen', 3: 'Thu', 4: 'Fri'}, inplace=True)
print(schedule)
print("leftover for next week is: \n" + str(next_week))    

