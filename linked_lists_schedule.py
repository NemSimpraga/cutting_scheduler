import pandas as pd
import data_model

class Day:                                                      #Day class: acts as a node in the Week class linked list
    def __init__(self, capacity):                                   #accepts capacity pd.Series as input parameter    
        self.capacity = capacity                                    #set the given capacity as the initialized node's initial capacity
        self.sum = self.capacity.sum()                              #set the node's total capacity as the sum of the set capacity attribute
        self.nextday = None                                         #set the pointer to the next node as None, by default
    def increase(self, cur_leftover):                                   #Increase method: increases the capacity of the current node
        self.grp_picked = cur_leftover.idxmax()                             #pick the group to which to add a carcass to the one with the most leftover capacity
        self.increment = data_model.stats['avg'][self.grp_picked]           #set the increment to be the average weight (best approximation) of the picked group
        self.capacity[self.grp_picked] += self.increment                    #increase the capacity of whichever group was picked
        self.sum = self.capacity.sum()                                      #refresh the total capacity after incrementing
        return self.grp_picked                                              #return the picked group
    def decrease(self):                                                 #Decrease method: decrease the capacity of the current node
        self.grp_picked = self.capacity.idxmax()                            #pick the group from which to take a carcass to the one with the most leftover capacity
        self.decrement = data_model.stats['avg'][self.grp_picked]           #set the decrement to be the average weight (best approximation) of the picked group
        self.capacity[self.grp_picked] -= self.decrement                    #decrease the capacity of whichever group was picked
        self.sum = self.capacity.sum()                                      #refresh the total capacity after decrementing
        return self.grp_picked                                              #return the picked group

class Week:                                                                                     #Week class: class implementation of linked lists, represents the whole current week
    def __init__(self):
        self.nextweek = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])      #cache used for storing capacity for next week
        self.leftover = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=['g1', 'g2', 'g3', 'g4', 'g5'])      #cache used for storing leftover capacity
        self.headval=None
    
    def optimise(self):                                                                                         #Optimise function: optimises the input schedule
        current = self.headval
        while current is not None:                                                                                  #Loop through nodes until end of list
            if current.sum > data_model.max_cap:                                                                    #if the total capacity of the current node is above the defined max capacity:
                while current.sum > data_model.max_cap:                                                                 #while the above statement is true
                    self.leftover[current.decrease()] += current.decrement                                              #decrease the current day using the decrease method and update the leftover of whichever group was picked
                current = current.nextday;                                                                          #when the capacity reaches the maximum, go to next day
            elif current.sum < data_model.max_cap and self.leftover.sum() > 0:                                      #if the total capacity of the current node is below the max capacity and there is leftover capacity from the previous days:
                while current.sum < (data_model.max_cap - data_model.stats['avg']['g1']) and self.leftover.sum() > 0:   #while the above statement is true
                    self.leftover[current.increase(self.leftover)] -= current.increment                                 #increase the current day using the increase method and update the leftover of whichever group was picked
                current = current.nextday;                                                                          #when the capacity reaches max or leftover is depleted, go to next day
            else: current = current.nextday;                                                                    #if day is under max cap OR day is over max cap but there is no leftover: do nothing, go to next day
        self.nextweek += self.leftover;                                                                     #after reaching end of list, add whatever is leftover to next week capacity



