#1. There are 3 syntax errors in the following code. Fix it to print correctly without errors. It will print, “Her name is Molly and her favorite food is tuna”.*/

food = "tuna"
name = "Molly"
print("Her name is " + name + " and her favorite food is " + food + ".")

#2. Let’s say that apples are $0.40 apiece, and pears are $0.65 apiece. Modify the program below to calculate the total cost of 4 apples and 3 pears.*/

apples = 4
pears = 3
totalCost = float(apples) * 0.40 + float(pears) * 0.65
print(totalCost)

#3. Take the phrase: twinkle twinkle little star. Store each word in a separate variable, then print out the sentence on one line using print.*/

v1 = "twinkle "
v2 = "twinkle "
v3 = "little "
v4 = "star"
print(v1+v2+v3+v4)

#4. Add parentheses to the following code so that the total equals 40.*/

total = (7 + 3) * (6 - 2)
print(total)

#5. Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on the clock when the alarm goes off. 
Using the int() function and modulus operator could come in handy!*/

current_time = input("What time is it now?")
waiting_time = input("How many hours do you wait for the alarm?")
int_ct = int(current_time)
int_wt = int(waiting_time)

hours = int_ct + int_wt 

hours_i_24 = hours % 24

print(hours_i_24)

#6 Assume that you have 24 slices of pizza and 7 people that are going to share it. 
There’s been some arguments among your friends, so you’ve decided to only give people whole slices. 
Your pet dog Andy loves pizza. 
Write a Python expression with the modulus operator that calculates 
how many pizza slices will be left over for your dog after serving just whole slices to 7 people. 
Assign the result of that expression to forAndy.*/

pizza = 24
people = 7
forAndy = pizza % people 
print(forAndy)

#7 Write a program that will convert inches to feet from user input. Reminder: there are 12 inches in a foot.*/
inches = int(input("How many inches?"))
feet = int(inches / 12)
print(inches, "inches is", feet, "feet.")

#8 Write a program that will convert feet to inches from user input. Reminder: there are 12 inches in a foot.*/
feet = int(input("How many feet?"))
inches = int(feet * 12)
print(feet, "inches is", inches, "feet.")

#9 Print: “270 is 4.0 hours and 30 minutes.”*/
totalMinutes = 270
numMinutes = totalMinutes % 60
numHours = (totalMinutes - numMinutes) / 60
print(totalMinutes, "is", numHours, "hours and", numMinutes, "minutes.")

#10 Write code below to get at least 3 values from the user using the input function and output a mad lib (which will use the input to tell a silly story).*/
TBC



