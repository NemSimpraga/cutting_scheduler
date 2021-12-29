import pandas as pd
import statisticss

class Day:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.sum = self.capacity.sum()
        self.nextday = None
    def increase(self):
        self.capacity += statisticss.decrement
        self.sum = self.capacity.sum()
    def decrease(self):
        self.capacity -= statisticss.decrement
        self.sum = self.capacity.sum()

class Week:
    def __init__(self):
        self.nextweek = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
        self.leftover = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
        self.headval=None
    
    def printschedule(self):
        current = self.headval
        while current is not None:
            print("Capacity of current day: \n " +str(current.capacity))
            print("Sum: " +str(current.sum))
            #print("Leftover of current day: \n " +str(current.leftover))
            current = current.nextday
    
    def optimise(self):
        current = self.headval
        while current is not None:
            if current.sum > statisticss.max_cap:
                while current.sum > statisticss.max_cap:
                    current.decrease()
                    if current.nextday is not None: 
                        current.nextday.capacity += statisticss.decrement
                        self.leftover += statisticss.decrement
                    else: self.nextweek += statisticss.decrement
                current = current.nextday
            elif current.sum < statisticss.max_cap and self.leftover.sum() > 0:
                while current.sum < (statisticss.max_cap + statisticss.decrement.sum()) and self.leftover.sum() > 0:
                    current.increase()
                    current.capacity -= statisticss.decrement
                    self.leftover -= statisticss.decrement
                current = current.nextday
            else: current = current.nextday
            

intake = pd.Series([120,50,70,10,10])   

Mon = Day(statisticss.prepare(pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])))
Tue = Day(statisticss.prepare(intake[0]))
Wen = Day(statisticss.prepare(intake[1]))
Thu = Day(statisticss.prepare(intake[2]))
Fri = Day(statisticss.prepare(intake[3]))

schedule = Week()
schedule.nextweek = statisticss.prepare(intake[4])
schedule.headval = Tue

Mon.nextday = Tue
Tue.nextday = Wen
Wen.nextday = Thu
Thu.nextday = Fri

schedule.printschedule()
print("##########################################################")
schedule.optimise()
schedule.printschedule()
