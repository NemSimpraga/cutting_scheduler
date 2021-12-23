# assumptions:
# -assuming friday intake is transferred to monday for cutting ("...Cutting can start the day after reception, at the earliest...","...cutting is executed on weekdays...")
# -assuming monday cut is zero since intake info from last week is unavailable

import pandas as pd

stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5, 5.3, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}
max_cap = 30000
df_stats = pd.DataFrame(stats)

to_cut = pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
leftovers = pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
slaughter_intake = pd.Series([120,70,20,100,80])

def cut(intake, day):
    
    return intake

def processing(animals, day):
    cut(to_cut, day)
    leftovers = pd.Series(animals*df_stats['avg']*df_stats['f'], index=['g1', 'g2', 'g3', 'g4', 'g5'])
    


#cutting = slaughter_intake.shift(1,fill_value=slaughter_intake[slaughter_intake.size-1])


for day, animals in enumerate(slaughter_intake):
    processing(animals, day)


  
#def calc_cut(intake):
#    calc = {
#        'mon' : pd.Series(slaughter_intake['mon']*df['avg'])*df['f'],
#        'tue' : pd.Series(slaughter_intake['tue']*df['avg'])*df['f'],
#        'wen' : pd.Series(slaughter_intake['wen']*df['avg'])*df['f'],
#        'thu' : pd.Series(slaughter_intake['thu']*df['avg'])*df['f'],
#        'fri' : pd.Series(slaughter_intake['fri']*df['avg'])*df['f']
#        }
#    calc_df = pd.DataFrame(calc)
#    return calc_df

    
    
    



    
    

