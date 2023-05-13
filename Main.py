#Strings - store a series of characters)
name = 'I am'
#print(type(name))
#print (name + " hungry!")


#Integers - Numbers
age = 30
#age = age + 1
age += 1
print (age)
print(type(age))
print (name + " " + str(age))


#Floats - Numbers with decimal
Mass = 200
print ("Your mass is: " + str(Mass))


#Boolean - True/False
Human = True
print("Are you Human? " + str(Human))


#Multiple Assignment = allows us to assign multiple variables at the same time in one line of code
Vegeta, Goku, Iron_Man = 100, 80, 100
Vegeta += Goku + Iron_Man
Goku = Iron_Man


print(Vegeta)
print(Goku)
print(Iron_Man)

#Length = gives length of characters
Batman = "Bruce Wayne"
print(len(Batman))

#Find = gives how many spaces a character is over
print(Batman.find("u"))

#Capitalize = Capitalize the first letter/word in a string
cow = "good milk"
print(cow.capitalize())

#upper = capitalizes everthing
print(cow.upper())

#lower = puts everything in lower case
candy = "DELICIOUS"
print(candy.lower())

#isdigit = will tell true or false if a string is numbers or letters
army = "100"
school = "Science"
print(army.isdigit())
print(school.isdigit())

#isalpha = will tell true/false if a strink is letters
print(school.isalpha())

