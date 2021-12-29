import pandas as pd

dict_schedule = {                                                                            
    'Mon' : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    'Tue' : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    'Wen' : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    'Thu' : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    'Fri' : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    'NX_week' : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    }                                                                                         
scheduleDF = pd.DataFrame(dict_schedule)     

dict_stats = {                                                                
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
} 
stats = pd.DataFrame(dict_stats)
decrement=pd.Series([stats.transpose()['g1'].product(), 
                       stats.transpose()['g2'].product(),
                       stats.transpose()['g3'].product(),
                       stats.transpose()['g4'].product(),
                       stats.transpose()['g5'].product()], 
                      index=['g1', 'g2', 'g3', 'g4', 'g5'])/10
max_cap = 30000

def prepare(sl_intake):                                         
    return sl_intake*stats['f']*stats['avg']


        