import pandas as pd

dict_schedule = {
    0 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']), 
    } 
schedule = pd.DataFrame(dict_schedule)

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
to_cut = pd.Series([12514.2859, 12857.14305, 6600, 6771.428436, 6942.857004], index=['g1', 'g2', 'g3', 'g4', 'g5'])


leftovers = cut(to_cut, 0)
print(schedule)


















































