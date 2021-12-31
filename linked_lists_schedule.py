import pandas as pd
import data_model

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
            current = current.nextday
        print("Next week: \n" + self.nextweek.to_string() + '\nsum ' +str(self.nextweek.sum()))
    
    def optimise(self):
        current = self.headval
        while current is not None:
            if current.sum > data_model.max_cap:
                while current.sum > data_model.max_cap:
                    current.decrease()
                    self.leftover += current.decrement
                current = current.nextday; 
            elif current.sum < data_model.max_cap and self.leftover.sum() > 0:
                while current.sum < data_model.max_cap and self.leftover.sum() > 0:
                    current.increase()
                    self.leftover -= current.decrement
                current = current.nextday; 
            else: current = current.nextday; 
        self.nextweek += self.leftover; 

intake = pd.Series([120,70,65,100,50])   

Mon = Day('Monday', data_model.n_deterministic(0))
Tue = Day('Tuesday', data_model.n_deterministic(intake[0]))
Wen = Day('Wednesday', data_model.n_deterministic(intake[1]))
Thu = Day('Thursday', data_model.n_deterministic(intake[2]))
Fri = Day('Friday', data_model.n_deterministic(intake[3]))

schedule = Week()
schedule.nextweek = data_model.n_deterministic(intake[4])
schedule.headval = Mon

Mon.nextday = Tue
Tue.nextday = Wen
Wen.nextday = Thu
Thu.nextday = Fri

print("Unoptimised schedule; capacities shown are ready for cutting the next day:")
print(data_model.create_table(Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek, schedule.leftover))
print("Schedule after being shifted to the right:")
print(data_model.create_table(Mon.capacity, Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek))

schedule.optimise()

print("Cutting schedule for specified intake plan, after optimisation:")
print(data_model.create_table(Mon.capacity, Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek))


