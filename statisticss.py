import pandas as pd
 
dict_stats = {                                                                
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
} 
stats = pd.DataFrame(dict_stats)
max_cap = 30000

def prepare(sl_intake):                                         
    return sl_intake*stats['f']*stats['avg']


        