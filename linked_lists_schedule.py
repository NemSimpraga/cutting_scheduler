import pandas as pd
import create_data_model

class Day:
    def __init__(self, name, capacity=None):
        self.capacity = capacity
        self.name = name
        self.decrement = capacity / 700
        self.sum = self.capacity.sum()
        self.nextday = None
    def increase(self):
        self.capacity += self.decrement
        self.sum = self.capacity.sum()
    def decrease(self):
        self.capacity -= self.decrement
        self.sum = self.capacity.sum()

class Week:
    def __init__(self):
        self.nextweek = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
        self.leftover = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])
        self.headval=None
    
    def printschedule(self):
        current = self.headval
        while current is not None:
            print(current.name +": \n" + current.capacity.to_string())
            print("Sum: " +str(current.sum))
            #print("Current leftover: \n " + str(self.leftover))
            current = current.nextday
    
    def optimise(self):
        current = self.headval
        while current is not None:
            if current.sum > create_data_model.max_cap:
                while current.sum > create_data_model.max_cap:
                    current.decrease()
                    self.leftover += current.decrement
                current = current.nextday; print("Leftover: \n" +self.leftover.to_string())
            elif current.sum < create_data_model.max_cap and self.leftover.sum() > 0:
                while current.sum < create_data_model.max_cap and self.leftover.sum() > 0:
                    current.increase()
                    self.leftover -= current.decrement
                current = current.nextday; print("Leftover: \n" +self.leftover.to_string())
            else: current = current.nextday; print("Leftover: \n" +self.leftover.to_string())
        self.nextweek += self.leftover; print("Leftover: \n" +self.leftover.to_string())

intake = pd.Series([10,500,40,300,10])   

Mon = Day('Monday', create_data_model.n_deterministic(0))
Tue = Day('Tuesday', create_data_model.n_deterministic(intake[0]))
Wen = Day('Wednesday', create_data_model.n_deterministic(intake[1]))
Thu = Day('Thursday', create_data_model.n_deterministic(intake[2]))
Fri = Day('Friday', create_data_model.n_deterministic(intake[3]))

schedule = Week()
schedule.nextweek = create_data_model.n_deterministic(intake[4])
schedule.headval = Mon

Mon.nextday = Tue
Tue.nextday = Wen
Wen.nextday = Thu
Thu.nextday = Fri

#schedule.printschedule()
print("##########################################################")
schedule.optimise()
#schedule.printschedule()
#print(schedule.nextweek)
