import numpy as np
import pandas as pd

stats = {
    "g1" : pd.Series([365, 4.9, 0.28571429], index=["avg", "stddev", "f"]),
    "g2" : pd.Series([375, 5.1, 0.28571429], index=["avg", "stddev", "f"]),
    "g3" : pd.Series([385, 5.0, 0.14285714], index=["avg", "stddev", "f"]),
    "g4" : pd.Series([395, 5.3, 0.14285714], index=["avg", "stddev", "f"]),
    "g5" : pd.Series([405, 5.9, 0.14285714], index=["avg", "stddev", "f"]),
}

df = pd.DataFrame(stats)

def calc_cut(intake_today):
    g1 = intake_today*df['g1']['f']*df['g1']['avg']
    g2 = intake_today*df['g2']['f']*df['g2']['avg']
    g3 = intake_today*df['g3']['f']*df['g3']['avg']
    g4 = intake_today*df['g4']['f']*df['g4']['avg']
    g5 = intake_today*df['g5']['f']*df['g5']['avg']
    return g1+g2+g3+g4+g5

intake = [120,70,20,100,80]

print = calc_cut(120)