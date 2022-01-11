import pandas as pd
import data_model
import linked_lists_schedule

# =============================================================================
# Menu logic: 
    # press number 1 to select the predefined intake plan
    # press number 2 to input an intake plan via the terminal
    # repeat input if anything else than 1 or 2 is selected
# =============================================================================
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
intake = pd.Series([0,0,0,0,0], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
while True:
    print("Choose 1 or 2 from menu below:")
    choice = str(input("    1) Premade intake plan from the cutting scheduler task \n"+
                   "    2) Define your own intake plan Mon through Fri \n"))
    if choice in ['1','2']: break

if choice == '1':
    intake = pd.Series([120,70,20,100,80], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])   
else:
    for day in week:
        animals = 'hehe'
        while animals.isdigit() is False:
            animals = input('Enter the number of animals for ' + day + '\n')
        intake[day] = int(animals)

print("\nDefined intake is: \n" + intake.to_string())

# =============================================================================
# Initializing the starting nodes, before optimisation:
    # send 0 animals into schedule for monday (clarification in Readme.md file)
    # all other intakes are shifted by one to the next day 
# =============================================================================
Mon = linked_lists_schedule.Day(data_model.distribute(0))
Tue = linked_lists_schedule.Day(data_model.distribute(intake['Mon']))
Wen = linked_lists_schedule.Day(data_model.distribute(intake['Tue']))
Thu = linked_lists_schedule.Day(data_model.distribute(intake['Wed']))
Fri = linked_lists_schedule.Day(data_model.distribute(intake['Thu']))

#Initialize the linked list and schedule intake from Friday for next week
schedule = linked_lists_schedule.Week()
schedule.nextweek = data_model.distribute(intake['Fri'])

#link the nodes in the list to eachother
schedule.headval = Mon
Mon.nextday = Tue
Tue.nextday = Wen
Wen.nextday = Thu
Thu.nextday = Fri

#printing out the schedule before optimisation
print("Schedule after slaughter; capacities shown are ready for cutting the next day:")
print(data_model.create_table(Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek, schedule.leftover)[0])
print("Schedule after being shifted to the right:")
print(data_model.create_table(Mon.capacity, Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek)[0])

schedule.optimise()         #schedule optimisation is initiated here

#print out the final, optimised schedule
print("Cutting schedule for specified intake plan, after optimisation:")
print(data_model.create_table(Mon.capacity, Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek)[0])
print("Optimised cutting schedule by animal numbers per day:")
print(data_model.create_table(Mon.capacity, Tue.capacity, Wen.capacity, Thu.capacity, Fri.capacity, schedule.nextweek)[1])

