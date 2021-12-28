#assumptions:
    #-monday cutting schedule is empty since monday intake can be cut on tuesday at the earliest
    #-last week's intake is not known
    #-friday intake is pushed to next week automatically since cutting can happen only on weekdays

import pandas as pd

dict_schedule = {                                                                            #empty schedule initialized as 
    0 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          #dictionary for better visibility
    1 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    2 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    3 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    4 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    5 : pd.Series([0, 0, 0, 0, 0, 0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),          
    }                                                                                         
schedule = pd.DataFrame(dict_schedule)                                                       #converting created schedule to pd.Dataframe
                                                                                                
dict_stats = {                                                                                                                                      #initialazing the given stats                                                                 
    'avg' : pd.Series([365, 375, 385, 395, 405, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714, 1], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum']),
} 
stats = pd.DataFrame(dict_stats)                                                             #converting stats to pd.Dataframe
stats['avg']['sum'] = stats.transpose().product().sum()                                      #calculating the aggregated average weight weight of an animal -> ~380.715
decrement=7*pd.Series([stats.transpose()['g1'].product(), stats.transpose()['g2'].product(),stats.transpose()['g3'].product(),stats.transpose()['g4'].product(),stats.transpose()['g5'].product(),stats.transpose()['sum'].product()], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])/100
                                                                                             #ABOVE LINE# -> creating a pd.Series to use for decrementing/incrementing schedule capacity, using the given stats to preserve weight ratios
next_week = pd.Series([0,0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5', 'sum'])            #initialising pd.Series for leftover weight for next week's cutting scheduke
max_cap = 30000

def prepare(sl_intake):                                         #function used to return pd.Series from integer number of intake animals, according to given stats
    return sl_intake*stats['f']*stats['avg']

intake = pd.Series([120,100,78,20,150])                           #defining this week's intake
for day, animals in enumerate(intake):                          #creating initial non-shifted & non-optimised schedule
    schedule[day]=prepare(animals)

before_optimisation = schedule.drop(columns=5)                  #savig non-optimised schedule
next_week = schedule[4]                                         #scheduling Friday's intake for next week
schedule = schedule.shift(1,axis=1, fill_value=0)             #shift whole schedule right by one day and fill in NaN values
schedule[5]=0                                                   #empty last column to be used for displaying next week schedule

i=0                                                             #counter used for looping through day to be decremented
j=0                                                             #counter used for looping through days to be incremented

                                                                #DISCLAIMER: I do realise the O(n)^2 (at the least) horribleness of the next bit of code :) 
for i in schedule:                                                              #for each day in schedule do the following:               
   while schedule[i]['sum'] > max_cap:                                            #while the total sum of the current day is more than _cap
       while schedule[j+i+1]['sum'] < max_cap-decrement['sum']:                   #while the total sum of each next day is more than max_cap
           schedule[i] = schedule[i].sub(decrement, axis='rows')                  #decrement the current day by the decrement array
           if j+i+1 <= 4:                                                         #if the next day is this week
               schedule[j+i+1] = schedule[j+i+1].add(decrement, axis='rows')        #then add the decremented amount to that next day
           else: next_week = next_week.add(decrement, axis='rows')                  #else add the decremented amount for next week
           if schedule[i]['sum'] <= max_cap:  i+= 1; break;  
       print(schedule)                                                            #if at any point during the decrementation of current day 
       if j+i+1 <= 4: j += 1;                                                                  #we reach the current day's max_cap, break the decrement loop and increase increment day by one

schedule[5] = next_week
schedule.rename(columns={0: 'Mon', 1: 'Tue', 2: 'Wen', 3: 'Thu', 4: 'Fri', 5: 'Nx_week'}, inplace=True)
before_optimisation.rename(columns={0: 'Mon', 1: 'Tue', 2: 'Wen', 3: 'Thu', 4: 'Fri', 5: 'Nx_week'}, inplace=True)
intake.rename(index={0: 'Mon', 1: 'Tue', 2: 'Wen', 3: 'Thu', 4: 'Fri'}, inplace=True)
print("Intake for this week, Mon - Fri is: \n" +str(intake))
print("After slaughter each day, the distribution per group is the following: \n" +str(before_optimisation))
print("After optimising for max capacity of 30000kg per day, the schedule is;: \n" +str(schedule))


