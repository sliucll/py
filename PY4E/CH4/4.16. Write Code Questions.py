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
    
/*10. 
