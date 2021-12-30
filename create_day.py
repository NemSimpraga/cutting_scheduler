import pandas as pd
import numpy as np

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5.0, 5.4, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5'])
}
stats = pd.DataFrame(dict_stats)

def create_model(animals):
    day = pd.Series([0.0,0.0,0.0,0.0,0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
    for animal in range(0,animals,1):
        choice = pd.Series([np.random.normal(loc=stats['avg']['g1'], scale=stats['stddev']['g1']), 
                            np.random.normal(loc=stats['avg']['g2'], scale=stats['stddev']['g2']),
                            np.random.normal(loc=stats['avg']['g3'], scale=stats['stddev']['g3']), 
                            np.random.normal(loc=stats['avg']['g4'], scale=stats['stddev']['g4']), 
                            np.random.normal(loc=stats['avg']['g5'], scale=stats['stddev']['g5'])], 
                           index=['g1', 'g2', 'g3', 'g4', 'g5'])
        picked = np.random.choice(choice, p=stats['f'])
        picked_grp= choice[choice == picked].index[0]
        day[picked_grp] += picked
    return day