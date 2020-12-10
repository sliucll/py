/*1. The code should print “The number is 5” when the number is 5, and should print “The number is NOT 5” when it is not.*/
x = 5
if x == 5:
    print("The number is 5")
else:
    print("The number is NOT 5")
    
/*2. Complete the conditional below so the word “Hi” is printed if x does not equal 3 and “Hello” is printed otherwise.*/
x = 4
if x != 3:
    print("Hi")
else:
    print("Hello")
    
/*3. Complete the pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours, if the regular pay rate is $10 an hour. 
Then set grossPay equal to the amount an employee would be paid for working 45 hours.*/
hours = 45
rate = 10
overtimeRate =  rate * 1.5
grossPay = 0
if hours  <= 40:
    grossPay = hours * rate
else:
    overTime =  hours % 40
    grossPay =  (rate * 40) + (overTime * overtimeRate)
print(grossPay)

/*4. Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 
The following shows two executions of the program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input */ 

hours=input("Enter Hours:")
try:
  int(hours)
  rate=input("Enter Rate:")
  int(rate)
  pay = int(hours) * int(rate) 
  int(pay)
  print("Pay:")
  print(pay)
except: 
  print("Error, please enter a number.  Please run the program again.")
  
/*5. Write the code to calculate and print the cost of a 14 mile cab ride. If the distance traveled is less than or equal to 12 miles the cost is $2.00 a mile, and 
if the distance traveled is more than 12 miles the cost is $1.50 a mile. Assign the final cost to the variable total.
distance = 14
if distance <= 12:
    rate = 2
if distance > 12:
    rate = 1.5
total = distance * rate
print("Total cost of trip:",total)

/*6. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
If the score is between 0.0 and 1.0, print a grade using the following table:
 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
Enter score: 0.95
A */
scr = input("Enter a score between 0.0 and 1.0...")
try:
   if float(scr) > 1.0 or float(scr) < 0.0:
       print("Bad score")
   elif float(scr) >= 0.9:
       print("A")
   elif float(scr) >= 0.8:
       print("B")
   elif float(scr) >= 0.7:
       print("C")
   elif float(scr) >= 0.6:
       print("D")
   elif float(scr) < 0.6:
       print("F")
except:
   print("Bad score")
   
/*7. Fix the example such that the cost of frozen yogurt is 0 if you pour exactly 1 lb. in your cup. */
weight = 0.5
if weight < 1:
    price = 1.45
if weight > 1:
    price = 1.15
if weight == 1:
    price = 0
total = weight * price
print(weight)
print(price)
print(total)

/*8. Write a procedure that takes 2 ints, total price, and amount in wallet. 
Print “You have enough money” if the difference between the wallet and price is 0 or greater; otherwise, print “Get more money”.
total_price = int(input("How much is your bill?"))
amount = int(input("How much do you have in your wallet?"))
if amount - total_price >= 0:
    print("You have enough money")
else:
    print("Get more money")
    
/*9. 3 criteria must be taken into account to identify leap years:

- The year is evenly divisible by 4;

- If the year can be evenly divided by 100, it is NOT a leap year, unless;

- The year is also evenly divisible by 400. Then it is a leap year.

Write a program that takes a year as a parameter and sets leapYear equal to True if the year is a leap year, False otherwise. 
(use a few different years to test your work) */
year = 2000
leapYear = False
if year % 400 == 0:
    leapYear = True
elif year % 4 == 0 and year % 100 != 0:
    leapYear = True
print(leapYear)

/*10. Write a program that takes an integer and sets isEven to True if the argument is an even number and False if it is odd. (the mod operator could be useful!)*/
def is_even(n):
    if n % 2 == 0:
        print(True)
    if n % 2 != 0:
        print(False)
        
is_even(888)



    



