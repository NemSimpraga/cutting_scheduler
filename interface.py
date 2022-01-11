import pandas as pd
import linked_lists_schedule
import data_model

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

Mon = linked_lists_schedule.Day('Monday', data_model.n_deterministic(0))
Tue = linked_lists_schedule.Day('Tuesday', data_model.n_deterministic(intake['Mon']))
Wen = linked_lists_schedule.Day('Wednesday', data_model.n_deterministic(intake['Tue']))
Thu = linked_lists_schedule.Day('Thursday', data_model.n_deterministic(intake['Wed']))
Fri = linked_lists_schedule.Day('Friday', data_model.n_deterministic(intake['Thu']))

schedule = linked_lists_schedule.Week()
schedule.nextweek = data_model.n_deterministic(intake['Fri'])

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
