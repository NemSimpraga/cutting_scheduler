import pandas as pd
import numpy as np

dict_schedule = {
    0 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    } 
schedule = pd.DataFrame(dict_schedule)

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5.0, 5.4, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5'])
}
stats = pd.DataFrame(dict_stats)
#stats['avg']['sum'] = stats.transpose().product().sum()
#decrement=pd.Series([stats.transpose()['g1'].product(), stats.transpose()['g2'].product(),stats.transpose()['g3'].product(),stats.transpose()['g4'].product(),stats.transpose()['g5'].product()], index=['g1', 'g2', 'g3', 'g4', 'g5'])
max_cap = 30000

intake = pd.Series([120,70,60,20,150]) 
day= pd.Series([0.0,0.0,0.0,0.0,0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])

for animal in range(0,120,1):
    choice = pd.Series([np.random.normal(loc=stats['avg']['g1'], scale=stats['stddev']['g1']), 
                        np.random.normal(loc=stats['avg']['g2'], scale=stats['stddev']['g2']),
                        np.random.normal(loc=stats['avg']['g3'], scale=stats['stddev']['g3']), 
                        np.random.normal(loc=stats['avg']['g4'], scale=stats['stddev']['g4']), 
                        np.random.normal(loc=stats['avg']['g5'], scale=stats['stddev']['g5'])], 
                       index=['g1', 'g2', 'g3', 'g4', 'g5'])
    picked = np.random.choice(choice, p=stats['f'])
    picked_grp= choice[choice == picked].index[0]
    day[picked_grp] += picked

print(day)
print(day.sum())



#print(prepare(120))

#decrement = pd.Series([choice['g1']*stats['f']['g1'], choice['g2']*stats['f']['g2'], choice['g3']*stats['f']['g3'], choice['g4']*stats['f']['g4'], choice['g5']*stats['f']['g5'], 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'suma'])
#decrement['suma'] = decrement.sum()
#print("Decrement will be done in: \n" +str(decrement))