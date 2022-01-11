# Cutting Scheduler
### Description:
The cutting scheduler project was created as an answer to the coding challenge that can be found on:
    https://github.com/volur-ai/recruitment/blob/main/developer/cutting-scheduler.ipynb

### Project content & libraries used
The solution to the cutting scheduler problem is containted in the 3 following Python modules:
* linked_lists_schedule.py
* data_model.py
* interface.py

Libraries used:
* pandas: used for storing and performing necessary calculations on the stored data
* numpy: used for creating the data model according to the given statistics table
* python v3.8.8.

### Modules description

##### linked_lists_schedule.py
Contains the Week and Day classes
- Week is a linked list implementation class which contains nodes - the Day class
- Week class has the _optimise_ method, which contains the optimisation logic
- Day class has the _increase_ and _decrease_ methods, used by the _optimise_ class to increase or decrease the current day's capacity

##### data_model.py
Contains the given statistics, function used to create the distribution model, and a function to create an easily printable table for showing output
- _distribute_ function - distributes the animals from the intake plan into their respective groups, while taking into consideration the given statistics
- _create_table_ - creates a pandas.Dataframe object from the given instances of the _Day_ class, formatted for output

##### interface.py
Contains the menu logic and printing functions
- the user can select between creating a sample intake plan according to the one given in the task (option '1') or inputting a plan themselves (option '2') 

### Solution logic 
The solution to the problem was based on the FIFO principle (_First In First Out)_:
1. Cut all carcasses as soon as you can, which is the following day
2. Any intake from Friday is automatically transferred to next week for cutting, since cutting can occur only on weekdays
3. Monday cutting schedule is empty because of fact #1) above and the assumption that we don't have the previous week's leftover intake
 
Specific optimisation logic is described in comments in the python files themselves

### Extra note
The solution has one flaw in the _data_model_ module, _distribute_ function:
- the data distribution model for each group is created via the numpy.random.normal function, which accepts the _loc_ (average weight), _scale_ (standard deviation) and _size_ (sample size) arguments
- the _size_ parameter_ is calculated by rounding the product of number of animals taken in and the frequency of every respective group
- the rounding of that parameter is what causes the schedule to sometimes miss or have one more animal than what is originally input for distribution
- if the output has one more or less animal than intended, depends on the modulus of animal intake and number 7, since the frequencies of g1, g2 vs g3, g4, g5 are 2/7 and 1/7 respectively
This flaw is patched by adding or removing one animal from a random group, depending on if the output is missing or has one more animal than intended