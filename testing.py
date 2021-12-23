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
    'stddev' : pd.Series([4.9, 5.1, 5, 5.3, 5.9], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}
stats = pd.DataFrame(dict_stats)

def cut(intake, day):
    current_cap = 0
    max_cap = 30000
    while current_cap < max_cap:
        if current_cap + 365*2 > max_cap:
            if current_cap + 365 > max_cap:
                break;
            else:
                intake['g1'] -= 365; 
                current_cap += 365;
                schedule[day]['g1'] += 365;
                break;
        intake['g1'] -= 365*2; current_cap += 365*2; schedule[day]['g1'] += 365*2;
        if current_cap + 375*2 > max_cap: 
            if current_cap + 375*2 > max_cap:
                if current_cap + 375 > max_cap:
                    break;
            else:
                intake['g2'] -= 375; 
                current_cap += 375;
                schedule[day]['g1'] += 375;
                break;
        intake['g2'] -= 375*2; current_cap += 375*2; schedule[day]['g2'] += 375*2;
        if current_cap + 385 > max_cap: break;
        intake['g3'] -= 385; current_cap += 385; schedule[day]['g3'] += 385;
        if current_cap + 395 > max_cap: break;
        intake['g4'] -= 395; current_cap += 395; schedule[day]['g4'] += 395;
        if current_cap + 405 > max_cap: break;
        intake['g5'] -= 405; current_cap += 405; schedule[day]['g5'] += 405;
    schedule[day]['sum'] = current_cap
    return intake

slaughter_intake = pd.Series([120,70,20,100,80])

def slaughter(sl_intake, day):
    return sl_intake*stats['f']*stats['avg'], day+1

for day, animals in enumerate(slaughter_intake):
    cut(slaughter(animals, day)

#print(schedule)
#to_cut = pd.Series([12514.2859, 12857.14305, 6600, 6771.428436, 6942.857004], index=['g1', 'g2', 'g3', 'g4', 'g5'])

















































