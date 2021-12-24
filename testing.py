import pandas as pd

test = pd.Series([12514.2859, 12857.14305, 6599.999868, 6771.428436, 6942.857004], index=['g1', 'g2', 'g3', 'g4', 'g5'])

dict_schedule = {
    5 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']), 
    } 
schedule = pd.DataFrame(dict_schedule)

increase = pd.Series([365*2, 375*2, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5'])

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}
stats = pd.DataFrame(dict_stats)



def slaughter(sl_intake):
    return sl_intake*stats['f']*stats['avg']

def cut(intake, day):
    current_cap = 0
    max_cap = 30000
    while current_cap < max_cap:
        if current_cap + increase['g1'] < max_cap and intake['g1'] >= increase['g1']:
            intake['g1'] -= increase['g1']; current_cap += increase['g1']; schedule[day+1]['g1'] += increase['g1'];
    schedule[day]['sum'] = current_cap
    return intake

slaughter_intake = pd.Series([120,70,20,100,80])

print(slaughter(slaughter_intake[0]))
#for day, animals in enumerate(slaughter_intake):
#    print(cut(slaughter(animals), day+1))
#
#print(schedule)

















































