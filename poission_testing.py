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
decrement=pd.Series([stats.transpose()['g1'].product(), stats.transpose()['g2'].product(),stats.transpose()['g3'].product(),stats.transpose()['g4'].product(),stats.transpose()['g5'].product(),stats.transpose()['sum'].product()], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])

next_week = pd.Series([0,0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])
max_cap = 30000

print(decrement['sum'])
print(decrement.sum())