import pandas as pd
import numpy as np
from scipy.stats import poisson, poisson_gen

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5.0, 5.4, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5'])
}
stats = pd.DataFrame(dict_stats)

max_cap = 30000

def n_deterministic(animals):
    distribution_g1 = np.random.normal(loc=stats['avg']['g1'], scale=stats['stddev']['g1'], size=round(stats['f']['g1']*animals))
    distribution_g2 = np.random.normal(loc=stats['avg']['g2'], scale=stats['stddev']['g2'], size=round(stats['f']['g2']*animals))
    distribution_g3 = np.random.normal(loc=stats['avg']['g3'], scale=stats['stddev']['g3'], size=round(stats['f']['g3']*animals))
    distribution_g4 = np.random.normal(loc=stats['avg']['g4'], scale=stats['stddev']['g4'], size=round(stats['f']['g4']*animals))
    distribution_g5 = np.random.normal(loc=stats['avg']['g5'], scale=stats['stddev']['g5'], size=round(stats['f']['g5']*animals))

    day = pd.Series([distribution_g1.sum(),distribution_g2.sum(),distribution_g3.sum(),distribution_g4.sum(),distribution_g5.sum()], 
                    index=['g1', 'g2', 'g3', 'g4', 'g5'])
    return day, day.sum(), animals*380.71

def deterministic(animals): 
    day = animals*stats['f']*stats['avg']                      
    return day, day.sum(), animals*380.71


def poisson(animals):
    day = poisson.rvs()
    return day

print(poisson(20))
