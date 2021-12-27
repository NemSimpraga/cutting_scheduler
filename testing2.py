import pandas as pd

dict_schedule = {
    0 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    5 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    } 
schedule = pd.DataFrame(dict_schedule)

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714, 1], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
}
stats = pd.DataFrame(dict_stats)
stats['avg']['sum'] = stats.transpose().product().sum()
decrement=7*pd.Series([stats.transpose()['g1'].product(), stats.transpose()['g2'].product(),stats.transpose()['g3'].product(),stats.transpose()['g4'].product(),stats.transpose()['g5'].product()/100,stats.transpose()['sum'].product()], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])/100

next_week = pd.Series([0,0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])
max_cap = 30000
avg_pday = max_cap / stats['avg']['sum']

def prepare(sl_intake):
    return sl_intake*stats['f']*stats['avg']

intake = pd.Series([1000,70,50,40,50])
for day, animals in enumerate(intake):
    schedule[day]=prepare(animals)


print(schedule)
next_week = schedule[4]
schedule = schedule.shift(1,axis=1)
schedule[5]=0
print(schedule)

i=0
j=0

for i in schedule:
   while schedule[i]['sum'] > 30000:
       while schedule[j+i+1]['sum'] < 30000-decrement['sum']:
           schedule[i] = schedule[i].sub(decrement, axis='rows')
           if j+i+1 <= 4:
               schedule[j+i+1] = schedule[j+i+1].add(decrement, axis='rows')
           else: next_week = next_week.add(decrement, axis='rows')
           if schedule[i]['sum'] <= 30000: break;
       j += 1;
       print(schedule)
  
print(schedule)
print(next_week)

