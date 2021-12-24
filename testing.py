import pandas as pd

dict_schedule = {
    5 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']), 
    } 
schedule = pd.DataFrame(dict_schedule)

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}

stats = pd.DataFrame(dict_stats)
increment = pd.Series([55, 55, 55, 55, 55], index=['g1', 'g2', 'g3', 'g4', 'g5'])

global leftover
leftover = pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5'])

def slaughter(sl_intake):
    return sl_intake*stats['f']*stats['avg']

def cut(intake, day):
    current_cap = 0
    max_cap = 30000
    while current_cap < max_cap:
        if intake ['g1'] > 0 and current_cap < max_cap: intake['g1'] -= increment['g1']; current_cap += increment['g1']; schedule[day+1]['g1'] += increment['g1'];
        if intake ['g1'] > 0 and current_cap < max_cap: intake['g1'] -= increment['g1']; current_cap += increment['g1']; schedule[day+1]['g1'] += increment['g1'];
        if intake ['g2'] > 0 and current_cap < max_cap: intake['g2'] -= increment['g2']; current_cap += increment['g2']; schedule[day+1]['g2'] += increment['g2'];
        if intake ['g2'] > 0 and current_cap < max_cap: intake['g2'] -= increment['g2']; current_cap += increment['g2']; schedule[day+1]['g2'] += increment['g2'];
        if intake ['g3'] > 0 and current_cap < max_cap: intake['g3'] -= increment['g3']; current_cap += increment['g3']; schedule[day+1]['g3'] += increment['g3'];
        if intake ['g4'] > 0 and current_cap < max_cap: intake['g4'] -= increment['g4']; current_cap += increment['g4']; schedule[day+1]['g4'] += increment['g4'];
        if intake ['g5'] > 0 and current_cap < max_cap: intake['g5'] -= increment['g5']; current_cap += increment['g5']; schedule[day+1]['g5'] += increment['g5'];
        if(intake ['g1'] < 5 and intake ['g2'] < 5 and intake ['g3'] < 5 and intake ['g4'] < 5 and intake ['g5'] < 5): break;
    schedule[day+1]['sum'] = current_cap
    global leftover
    leftover = intake
    
    
#slaughter_intake = pd.Series([80,90,40,60,120])
#slaughter_intake = pd.Series([60,70,50,100,110])
#slaughter_intake = pd.Series([95,45,110,120,20])
#slaughter_intake = pd.Series([82,150,40,30,78])
slaughter_intake = pd.Series([150,60,100,45,35])

for day, animals in enumerate(slaughter_intake):
    cut(slaughter(animals)+leftover, day)

print(schedule)
print(schedule[5]['sum']+schedule[1]['sum']+schedule[2]['sum']+schedule[3]['sum']+schedule[4]['sum'])



















































