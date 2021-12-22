#   assumptions:
# -friday intake is transferred to monday for cutting ("...Cutting can start the day after reception, at the earliest...","...cutting is executed on weekdays...")
# -output table shows friday's intake on this week's monday

import pandas as pd

#stats = {
#    'g1' : pd.Series([365, 4.9, 0.28571429], index=['avg', 'stddev', 'f']),
#    'g2' : pd.Series([375, 5.1, 0.28571429], index=['avg', 'stddev', 'f']),
#    'g3' : pd.Series([385, 5.0, 0.14285714], index=['avg', 'stddev', 'f']),
#    'g4' : pd.Series([395, 5.3, 0.14285714], index=['avg', 'stddev', 'f']),
#    'g5' : pd.Series([405, 5.9, 0.14285714], index=['avg', 'stddev', 'f']),
#}

stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5, 5.3, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}

max_cap = 30000
df = pd.DataFrame(stats)

slaughter_intake = pd.Series([120,70,20,100,80], index=['mon', 'tue', 'wen', 'thu', 'fri'])
cutting_intake = slaughter_intake.shift(1,fill_value=slaughter_intake[slaughter_intake.size-1])

def calc_cut(intake):
    calc = {
        'mon' : pd.Series(slaughter_intake['mon']*df['avg'])*df['f'],
        'tue' : pd.Series(slaughter_intake['tue']*df['avg'])*df['f'],
        'wen' : pd.Series(slaughter_intake['wen']*df['avg'])*df['f'],
        'thu' : pd.Series(slaughter_intake['thu']*df['avg'])*df['f'],
        'fri' : pd.Series(slaughter_intake['fri']*df['avg'])*df['f']
        }
    calc_df = pd.DataFrame(calc)
    print(calc_df)
    
calc_cut(slaughter_intake)
    
    
    



    
    

