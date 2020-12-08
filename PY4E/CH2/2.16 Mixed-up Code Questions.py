/*Q-1: The following program segment should prompt the user for their name and say hello to them.*/
name = input('What is your name?')
greeting = "Hello "
print(greeting + name)

/*Q-2: The following program segment should print the phrase, "Carla loves lemons."*/
feeling = "loves"
print("Carla " + feeling + "lemons.")

/*Q-3: The following program segment should ask the user their hours per week and pay rate, then print a statement with their gross pay.*/
hours = input('How many hours do you work in a week?')
payRate = input('What is your hourly pay?')
grossPay = float(hours) * float(payRate)
print("Your gross pay is ", grossPay)

/*Q-4: The following program segment should print out the cost for each shirt if they are to buy 2 and get the third free but were originally $45 each.*/
price = 45
totalCost = price * 2
pricePerShirt = totalCost / 3
print(pricePerShirt)

/*Q-5: The following program segment should print out the cost per person for a dinner including the tip.*/
bill = 89.23
tip = bill * 0.20
total = bill + tip
numPeople = 3
perPersonCost = total / numPeople
print(perPersonCost)

/*Q-6: The following program segment should swap the values of x and y after val1 and val 2 are assigned to x and y, respectively.*/
x = val1
y = val2
temp = x
x = y
y = temp

/*Q-7: The following program segment should print how much you will have to pay for an item that is 60% off the original price of $52.99.*/
price = 52.99
discount = 0.6
savings = price * discount
finalPrice = price - savings
print(finalPrice)

/*Q-8: The following program segment should print the phrase, "Baking cookies makes Chris happier than anything else.".*/
var1 = "cookies"
print("Baking " + var1 + " makes Chris happier than anything else.")

/*Q-9: The following program segment should print the phrase, "It takes us 2 hours and 45 minutes to get home from camp.".*/
numHours = 2
numMinutes = 45.0
print("It takes us " + str(numHours) + " hours and " + str(numMinutes) + " minutes to get home from camp.")

/*Q-10: The following program segment should print the phrase, "3 + 300 + 7 = 310.".*/
num1 = 3
num2 = 300
num3 = 7
ans = 310
print(str(num1) + " + " + str(num2) + " + " + str(num3) + " = " + str(ans))

/*
