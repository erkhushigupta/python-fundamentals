#Program to reserve a table at a restaurant if any amount is paid.

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'? "))

if money: 
	print("Ah, I am reminded of a table. Right this way.")
else:
	print("Please, sit. It may be a while.")

input("\n\nPress the enter key to exit.")

#If money is paid ,a table will be reserved
#If no money is paid then person will have to wait.


#input: 0
#expected output: Welcome to the Chateau D' Food
#It seems we are quite full this evening.

#Please, sit. It may be a while.



#input: 100
#expected output:Welcome to the Chateau D' Food
#It seems we are quite full this evening.

#Ah, I am reminded of a table. Right this way.
#'100'