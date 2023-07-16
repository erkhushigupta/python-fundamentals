#this function is defined to fill in for no existing entry,in this case country

#this is useful to avoid blank unanswered questions

def my_function(country ="India") :
 print("I am from " + country)
my_function("Sweden")
my_function("Norway")
my_function()
my_function("Brazil")

#expected output:
#I am from Sweden
#I am from Norway
#I am from India
#I am from Brazil