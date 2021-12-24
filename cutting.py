# assumptions:
# -assuming friday intake is transferred to monday for cutting ("...Cutting can start the day after reception, at the earliest...","...cutting is executed on weekdays...")
# -assuming monday cut is zero since intake info from last week is unavailable

import pandas as pd

dict_schedule = {
    0 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']), 
    } 
schedule = pd.DataFrame(dict_schedule)

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'stddev' : pd.Series([4.9, 5.1, 5, 5.3, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}
stats = pd.DataFrame(dict_stats)

to_cut = pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
leftovers = pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
slaughter_intake = pd.Series([120,70,20,100,80])

def cut(intake, day):
    
    return intake

def processing(animals, day):
    cut(to_cut, day)
    leftovers = pd.Series(animals*stats['avg']*stats['f'], index=['g1', 'g2', 'g3', 'g4', 'g5'])
    

for day, animals in enumerate(slaughter_intake):
    processing(animals, day)


 def cut(intake, day):
    current_cap = 0
    max_cap = 30000
    while current_cap < max_cap:
        if current_cap + 365*2 > max_cap and current_cap + 365 > max_cap: 
            break;
        elif current_cap + 365 < max_cap and intake['g1'] > 0:
            intake['g1'] -= 365; 
            current_cap += 365;
            schedule[day]['g1'] += 365;
        if intake['g1'] > 0: intake['g1'] -= 365*2; current_cap += 365*2; schedule[day]['g1'] += 365*2;
        if current_cap + 375*2 > max_cap and current_cap + 375 > max_cap: 
            break;
        elif current_cap + 375 < max_cap and intake['g2'] > 0:
            intake['g2'] -= 375; 
            current_cap += 375;
            schedule[day]['g2'] += 375;
        if intake['g2'] > 0: intake['g2'] -= 375*2; current_cap += 375*2; schedule[day]['g2'] += 375*2;
        if current_cap + 385 > max_cap or intake['g3'] < 0: break;
        if intake['g3'] > 0: intake['g3'] -= 385; current_cap += 385; schedule[day]['g3'] += 385;
        if current_cap + 395 > max_cap: break;
        if intake['g4'] > 0: intake['g4'] -= 395; current_cap += 395; schedule[day]['g4'] += 395;
        if current_cap + 405 > max_cap: break;
        if intake['g5'] > 0: intake['g5'] -= 405; current_cap += 405; schedule[day]['g5'] += 405;
    schedule[day]['sum'] = current_cap
    return intake
 
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

    
    
    



    
    

