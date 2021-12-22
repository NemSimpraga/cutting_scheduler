#   assumptions:
# -friday intake is transferred to monday for cutting ("...Cutting can start the day after reception, at the earliest...","...cutting is executed on weekdays...")
# -output table shows friday's intake on this week's monday

import pandas as pd

stats = {
    'g1' : pd.Series([365, 4.9, 0.28571429], index=['avg', 'stddev', 'f']),
    'g2' : pd.Series([375, 5.1, 0.28571429], index=['avg', 'stddev', 'f']),
    'g3' : pd.Series([385, 5.0, 0.14285714], index=['avg', 'stddev', 'f']),
    'g4' : pd.Series([395, 5.3, 0.14285714], index=['avg', 'stddev', 'f']),
    'g5' : pd.Series([405, 5.9, 0.14285714], index=['avg', 'stddev', 'f']),
}
max_cap = 30000
df = pd.DataFrame(stats)

slaughter_intake = pd.Series([120,70,20,100,80], index=['mon', 'tue', 'wen', 'thu', 'fri'])
cutting_intake = slaughter_intake.shift(1,fill_value=slaughter_intake[slaughter_intake.size-1])

def calc_cut(intake_today):
    g1 = intake_today*df['g1']['f']*df['g1']['avg']
    g2 = intake_today*df['g2']['f']*df['g2']['avg']
    g3 = intake_today*df['g3']['f']*df['g3']['avg']
    g4 = intake_today*df['g4']['f']*df['g4']['avg']
    g5 = intake_today*df['g5']['f']*df['g5']['avg']
    

