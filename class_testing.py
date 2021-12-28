import pandas as pd

dict_stats = {                                                                
    'avg' : pd.Series([365, 375, 385, 395, 405], index=['g1', 'g2', 'g3', 'g4', 'g5']),
    'f' : pd.Series([0.28571429, 0.28571429, 0.14285714, 0.14285714, 0.14285714], index=['g1', 'g2', 'g3', 'g4', 'g5']),
} 
stats = pd.DataFrame(dict_stats)
decrement=pd.Series([stats.transpose()['g1'].product(), 
                       stats.transpose()['g2'].product(),
                       stats.transpose()['g3'].product(),
                       stats.transpose()['g4'].product(),
                       stats.transpose()['g5'].product()], 
                      index=['g1', 'g2', 'g3', 'g4', 'g5'])/100

def prepare(sl_intake):                                         
    return sl_intake*stats['f']*stats['avg']

class Day:
    def __init__(self, intake):
        self.capacity = intake
        self.sum = self.capacity.sum()
    def increase(self):
        self.capacity += decrement
        self.sum = self.capacity.sum()
    def decrease(self):
        self.capacity -= decrement
        self.sum = self.capacity.sum()
    def show(self):
        print(str(self.capacity) +"\n"+ str(self.capacity.sum()))
    
intake = pd.Series([120,100,78,20,150])
    
Mon = Day(pd.Series([0,0,0,0,0], index=['g1', 'g2', 'g3', 'g4', 'g5']))
Tue = Day(prepare(intake[0]))
Wen = Day(prepare(intake[1]))
Thu = Day(prepare(intake[2]))
Fri = Day(prepare(intake[3]))
next_week = prepare(intake[4])

Mon.show()
Tue.show()
Wen.show()
Thu.show()
Fri.show()
