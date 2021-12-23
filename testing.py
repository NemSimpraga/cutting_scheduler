import pandas as pd


schedule = {
    'mon' : pd.Series([0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'tue' : pd.Series([0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'wen' : pd.Series([0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'thu' : pd.Series([0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'fri' : pd.Series([0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
    } 

to_cut = pd.Series([12514.2859, 12857.14305, 6600, 6771.428436, 6942.857004], index=['g1', 'g2', 'g3', 'g4', 'g5'])
max_cap = 30000

def cut(intake):
    current_cap = 0
    while current_cap < max_cap:
        if current_cap + 365*2 > max_cap: 
            intake['g1'] -= 365; 
            current_cap += 365; 
            break;
        intake['g1'] -= 365*2; current_cap += 365*2; print("g1 leftover: "+str(intake['g1']))
        if current_cap + 375*2 > max_cap: intake['g2'] -= 375; current_cap += 375; break;
        intake['g2'] -= 375*2; current_cap += 375*2; print("g2 leftover: "+str(intake['g2']))
        if current_cap + 385 > max_cap: break;
        intake['g3'] -= 385; current_cap += 385; print("g3 leftover: "+str(intake['g3']))
        if current_cap + 395 > max_cap: break;
        intake['g4'] -= 395; current_cap += 395; print("g4 leftover: "+str(intake['g4']))
        if current_cap + 405 > max_cap: break;
        intake['g5'] -= 405; current_cap += 405; print("g5 leftover: "+str(intake['g5']))
    print(current_cap)
    return intake

print(cut(to_cut))