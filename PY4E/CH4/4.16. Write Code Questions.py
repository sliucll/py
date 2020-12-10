/*1. Fix the 4 errors so the following code runs and returns the perimeter of a rectangle.*/
def recPerimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
    
/*2. Fix the 5 errors so the following code runs and returns the area of a square.*/
def squareArea(length):
    area = length * length
    return area

/*3. Change the code so the function takes parameters for the base and height of the triangle. Then, write code to call the function and print the result.*/
def areaTriangle(base, height):
    area = (base * height) // 2
    return area
    
/*4. Change the code below to create a function tripCost that calculates the cost of a trip. 
It should take the miles, milesPerGallon, and pricePerGallon as parameters and should return the cost of the trip.*/
def tripCost(miles,milesPerGallon,pricePerGallon):
    total = (miles / milesPerGallon) * pricePerGallon
    return total

tripCost(500,26,3.45)

/*5. Fix the errors on line 2 so the function nameAndAge returns the string “My name is name and I am age years old.” 
The function call below should print “My name is John and I am 18 years old.”*/
def nameAndAge(nameString, ageInt):
    return("My name is "+nameString+" and I am "+str(ageInt)+" years old.")

print(nameAndAge("John", 18))

/*6. Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string. 
If someone enters an invalid score, return ‘Bad score’.
Score    Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6      F

def computegrade(r):
    try:
        if r >= 1.0:
            return "Bad score"
        elif r >= 0.9:
            return "A"
        elif r >= 0.8:
            return "B"
        elif r >= 0.7:
            return "C"
        elif r >= 0.6:
            return "D"
        elif r < 0.6:
            return "F"

    except:
        return('Bad score')

/*7. Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. 
So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.*/
def sumTo(n):
    result = (n * (n + 1)) / 2
    return result
    
/*8. Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n. 
This time use the accumulator pattern.*/
def sumTo(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

/*9. Write a function areaOfCircle(r)` which returns the area of a circle of radius r. Make sure you import the math module in your solution.*/
import math
def areaOfCircle(r):
    area = math.pi * r * r
    return area
    
/*10. Finish the function to return the average of a list of numbers, but drop the lowest value. However, if the list only has one value then return that. 
For example, get_avg_drop_lowest([90]) returns 90 and get_avg_drop_lowest([90, 10]) also returns 90.*/
def get_avg_drop_lowest(num_list):
    total = sum(num_list)
    lowest = min(num_list)
    num = len(num_list)
    if num == 1:
        return total
    else:
        return (total - lowest) / (num - 1)

/*11. Finish the function below to return the middle characters from the passed string. 
If the string has less than 3 characters then return the passed string. 
If the string has an odd length then return the middle character. 
If the string has an even length return the two middle characters. 
For example, get_middle(‘abc’) returns ‘b’ and get_middle(‘abcd’) returns ‘bc’.
def get_middle(str):
    num_chars =len(str)
    mid = num_chars // 2
    if num_chars < 3:
        return str
    elif num_chars % 2 == 1:
        return str[mid]
    else:
        return str[mid-1:mid+1]
    
/*12. You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. Unless it is your birthday – on that day, your speed can be 5 higher in all cases.*/
def caught_speeding(speed, is_birthday):
    if is_birthday is True:
        if speed <= 65:
            return 0
        elif speed <= 85:
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif speed <= 80:
            return 1
        else:
            return 2

/*13. Finish the function below to return ‘too low’ if the guess is less than the passed target, ‘correct’ if they are equal, and 
‘too high’ if the guess is greater than the passed target. 
For example, check_guess(5,7) returns ‘too low’, check_guess(7,7) returns ‘correct’, and check_guess(9,7) returns ‘too high’.*/
def check_guess(guess, target):
    if guess < target:
        return 'too low'
    elif guess == target:
        return 'correct'
    else:
        return 'too high'

/*14. Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, …6=Sat, and 
a boolean indicating if we are on vacation, return a string of the form “7:00” indicating when the alarm clock should ring. 
If we are on vacation and it is a weekend (0 - Saturday or 6 - Sunday) it should return “off” and otherwise return “10:00”. 
If we are not on vacation and it is a weekend it should return “10:00” and otherwise “7:00”*/
def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return 'off'
        else: 
            return '10:00'
    else:
        if day == 0 or day == 6:
            return '10:00'
        else: 
            return '7:00'


