import pandas as pd

#max = 148478.5713

dict_schedule = {
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    5 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']), 
    } 
schedule = pd.DataFrame(dict_schedule)

dict_stats = {
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
}
stats = pd.DataFrame(dict_stats)

def update_schedule(prepared, leftover, day):
    schedule[day+1] += prepared
    if leftover.any() != 0:
        schedule[(day+2)] += leftover 
        
        

def slaughter(sl_intake):
    return sl_intake*stats['f']*stats['avg']

def prepare(intake, day):
    leftover = intake
    prepared = pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
    decrement = pd.Series([5, 5, 2.5, 2.5, 2.5], index=['g1', 'g2', 'g3', 'g4', 'g5'])
    max_cap = 30000
    
    while (prepared.sum() < max_cap and leftover.any() > 5): 
        leftover = leftover - decrement
        prepared = intake - leftover    
        
    update_schedule(prepared, leftover, day)
        
 
#slaughter_intake = pd.Series([80,90,40,60,120])
#slaughter_intake = pd.Series([60,70,50,100,110])
#slaughter_intake = pd.Series([95,45,110,120,20])
slaughter_intake = pd.Series([120,70,20,100,80])
#slaughter_intake = pd.Series([150,60,100,45,35])

for day, animals in enumerate(slaughter_intake):
    prepare(slaughter(animals), day)

schedule.rename(columns={1: 'Mon', 2: 'Tue', 3: 'Wen', 4: 'Thu', 5: 'Fri'}, inplace=True)
#print(schedule['Mon']['sum']+schedule['Tue']['sum']+schedule['Wen']['sum']+schedule['Thu']['sum']+schedule['Fri']['sum'])



















































