import pandas as pd
import numpy as np
   
dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5.0, 5.4, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5'])
}
stats = pd.DataFrame(dict_stats)
agg_avg = stats['avg']['g1']*stats['f']['g1']+stats['avg']['g2']*stats['f']['g2']+stats['avg']['g3']*stats['f']['g3']+stats['avg']['g4']*stats['f']['g4']+stats['avg']['g5']*stats['f']['g5']
max_cap = 30000

def n_deterministic(animals):
    distribution_g1 = np.random.normal(loc=stats['avg']['g1'], scale=stats['stddev']['g1'], size=round(stats['f']['g1']*animals))
    distribution_g2 = np.random.normal(loc=stats['avg']['g2'], scale=stats['stddev']['g2'], size=round(stats['f']['g2']*animals))
    distribution_g3 = np.random.normal(loc=stats['avg']['g3'], scale=stats['stddev']['g3'], size=round(stats['f']['g3']*animals))
    distribution_g4 = np.random.normal(loc=stats['avg']['g4'], scale=stats['stddev']['g4'], size=round(stats['f']['g4']*animals))
    distribution_g5 = np.random.normal(loc=stats['avg']['g5'], scale=stats['stddev']['g5'], size=round(stats['f']['g5']*animals))
    
    day = pd.Series([distribution_g1.sum(),distribution_g2.sum(),distribution_g3.sum(),distribution_g4.sum(),distribution_g5.sum()], 
                    index=['g1', 'g2', 'g3', 'g4', 'g5'])
    return day

def deterministic(animals): 
    day = animals*stats['f']*stats['avg']                      
    return day

def create_table(mon,tue,wen,thu,fri,nxweek):
    dict_schedule = {                                                                            
    'Mon' : mon.append(pd.Series([mon.sum()], index=['sum'])),          
    'Tue' : tue.append(pd.Series([tue.sum()], index=['sum'])),         
    'Wed' : wen.append(pd.Series([wen.sum()], index=['sum'])),         
    'Thu' : thu.append(pd.Series([thu.sum()], index=['sum'])),          
    'Fri' : fri.append(pd.Series([fri.sum()], index=['sum'])),
    'Next week' : nxweek.append(pd.Series([nxweek.sum()], index=['sum'])),
    }                                                                                         
    return pd.DataFrame(dict_schedule).to_string()

animals = "120f"
print(animals.isdigit())
