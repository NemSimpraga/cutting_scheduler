import pandas as pd
import numpy as np

# defining given statistics (avg weight, frequency, standard, deviation, maximum capacity, aggregated average weight of animal)
dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5.0, 5.4, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5'])
}
stats = pd.DataFrame(dict_stats)
max_cap = 30000
agg_avg = stats['avg']['g1']*stats['f']['g1']+stats['avg']['g2']*stats['f']['g2']+stats['avg']['g3']*stats['f']['g3']+stats['avg']['g4']*stats['f']['g4']+stats['avg']['g5']*stats['f']['g5']

# =============================================================================
# Distribute function: distributes the animals according to the given statistics using the np.random.normal function
# lines 28 -> 33 : patching the potential missing or extra animals produced by the flaw in the distribution function
# =============================================================================
def distribute(animals):
    distribution_g1 = np.random.normal(loc=stats['avg']['g1'], scale=stats['stddev']['g1'], size=round(stats['f']['g1']*animals))
    distribution_g2 = np.random.normal(loc=stats['avg']['g2'], scale=stats['stddev']['g2'], size=round(stats['f']['g2']*animals))
    distribution_g3 = np.random.normal(loc=stats['avg']['g3'], scale=stats['stddev']['g3'], size=round(stats['f']['g3']*animals))
    distribution_g4 = np.random.normal(loc=stats['avg']['g4'], scale=stats['stddev']['g4'], size=round(stats['f']['g4']*animals))
    distribution_g5 = np.random.normal(loc=stats['avg']['g5'], scale=stats['stddev']['g5'], size=round(stats['f']['g5']*animals))
    
    day = pd.Series([distribution_g1.sum(),distribution_g2.sum(),distribution_g3.sum(),distribution_g4.sum(),distribution_g5.sum()], 
                    index=['g1', 'g2', 'g3', 'g4', 'g5'])

    if round(day.sum() / agg_avg) < animals:
        choice = np.random.choice(['g1', 'g2', 'g3', 'g4', 'g5'])
        day[choice] += stats['avg'][choice]
    elif round(day.sum() / agg_avg) > animals:
        choice = np.random.choice(['g1', 'g2', 'g3', 'g4', 'g5'])
        day[choice] -= stats['avg'][choice]
        
    return day
# =============================================================================
# Create table function: returns a properly formatted table for printing
#   df_schedule = dataframe containing group weight distributions
#   df_schedule_num = dataframe containing number of animals distribution, in integers
# =============================================================================

def create_table(mon,tue,wed,thu,fri,nxweek):
    dict_schedule = {                                                                            
    'Mon' : mon.append(pd.Series([mon.sum()], index=['sum'])),          
    'Tue' : tue.append(pd.Series([tue.sum()], index=['sum'])),         
    'Wed' : wed.append(pd.Series([wed.sum()], index=['sum'])),         
    'Thu' : thu.append(pd.Series([thu.sum()], index=['sum'])),          
    'Fri' : fri.append(pd.Series([fri.sum()], index=['sum'])),
    'Next week' : nxweek.append(pd.Series([nxweek.sum()], index=['sum'])),
    }           
    df_schedule = pd.DataFrame(dict_schedule) 
    df_schedule_num = round(df_schedule.div(stats['avg'], axis='rows'))
    df_schedule_num.at['sum', 'Mon'] = df_schedule_num['Mon'].sum()
    df_schedule_num.at['sum', 'Tue'] = df_schedule_num['Tue'].sum() 
    df_schedule_num.at['sum', 'Wed'] = df_schedule_num['Wed'].sum() 
    df_schedule_num.at['sum', 'Thu'] = df_schedule_num['Thu'].sum() 
    df_schedule_num.at['sum', 'Fri'] = df_schedule_num['Fri'].sum()       
    df_schedule_num.at['sum', 'Next week'] = df_schedule_num['Next week'].sum()                                        
    return df_schedule.to_string(), df_schedule_num.to_string()
