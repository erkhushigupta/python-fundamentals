#adding elements into a dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print(dict)
print(len (dict))
print(type (dict)) 
dict.keys



#expected output:
#{'Name': 'Zara', 'Age': 8, 'Class': 'First', 'School': 'DPS School'}
#4
#<class 'dict'>
#<function dict.keys>