import pandas as pd
import data_model

# =============================================================================
# Class day, which is a node 
# =============================================================================
class Day:                                                                                    
    def __init__(self, name, capacity=None):                                                        
        self.capacity = capacity
        self.name = namegdfgwdasd
        self.sum = self.capacity.sum()
        self.nextday = None
    def increase(self, cur_leftover):
        self.grp_picked = cur_leftover.idxmax()
        self.increment = data_model.stats['avg'][self.grp_picked]
        self.capacity[self.grp_picked] += self.increment
        self.sum = self.capacity.sum()
        return self.grp_picked
    def decrease(self):
        self.grp_picked = self.capacity.idxmax()
        self.decrement = data_model.stats['avg'][self.grp_picked]
        self.capacity[self.grp_picked] -= self.decrement
        self.sum = self.capacity.sum()
        return self.grp_picked

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
                    self.leftover[current.decrease()] += current.decrement
                current = current.nextday; 
            elif current.sum < data_model.max_cap and self.leftover.sum() > 0:
                while current.sum < (data_model.max_cap - data_model.stats['avg']['g1']) and self.leftover.sum() > 0:
                    self.leftover[current.increase(self.leftover)] -= current.increment
                current = current.nextday; 
            else: current = current.nextday; 
        self.nextweek += self.leftover; 



