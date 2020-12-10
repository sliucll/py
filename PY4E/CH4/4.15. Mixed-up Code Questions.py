/*Q-1: Use a built-in function to print out the length of sentence_a.*/
sentence_a = "I love Python!"
length_sentence_a = len(sentence_a)
print(length_sentence_a)

/*Q-2: Create a function called bmi that takes height and weight as parameters. It should return BMImetric.*/
def bmi(height, weight):
    heightSquared = height * height
    BMI = weight / heightSquared
    BMImetric = BMI * 703
    return BMImetric

/*Q-3: Create two functions. The first is called square, which returns a number squared. 
The second is called sum_of_squares, which returns the sum of the squares of three numbers.*/
def square(x):
    y = x * x
    return y
def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a + b + c

/*Q-4: Create a function called add_odd, which will add up the odd numbers from 1 (inclusive) to num (inclusive). 
The function should return the_sum. For example, add_odd(3) returns 4 since 1 + 3 = 4.*/
def add_odd(num):
    the_sum = 0
    for counter in range(num + 1):
        if counter % 2 == 1:
            the_sum = counter + 1
    return the_sum
    
/*Q-5: Create a function called addByThree, which will add three to the total num times. 
The function should return the total. 
for example, addByThree(2) returns 6 (3 + 3) and addByThree(3) returns 9 (3 + 3 + 3).*/
def addByThree(num):
    total = 0
    for counter in range(num):
        total = total + 3
    return total

/*Q-6: Create the function get_avg_drop_lowest to return the average of a list of numbers, but drop the lowest value. However, if the list only has one value then return that. 
For example, get_avg_drop_lowest([90]) returns 90 and get_avg_drop_lowest([90, 10]) also returns 90.*/
def get_avg_drop_lowest(num_list):
    total = sum(num_list)
    lowest = min(num_list)
    num = len(num_list)
    if num == 1:
        return total
    else:
        return (total - lowest) / (num - 1)
        
/*Q-7: Put the code blocks in order below to return the middle characters from the passed string. 
If the string has less than 3 characters then return the passed string. If the string has an odd length then return the middle character. 
If the string has an even length return the two middle characters. For example, get_middle(‘abc’) returns ‘b’ and get_middle(‘abcd’) returns ‘bc’.*?
def get_middle(str):
    num_chars =len(str)
    mid = num_chars // 2
    if num_chars < 3:
        return str
    elif num_chars % 2 == 1:
        return str[mid]
    else:
        return str[mid-1:mid+1]
        
/*Q-8: You are driving a little too fast, and a police officer stops you. 
Place the code blocks to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.*/
def caught_speeding(speed,is_birthday):
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

/*Q-9: Place the code blocks below to return 'too low' if the guess is less than the passed target, 
'correct' if they are equal, and 'too high' if the guess is greater than the passed target. 
For example, check_guess(5,7) returns 'too low', check_guess(7,7) returns 'correct', and check_guess(9,7) returns 'too high'.
def check_guess(guess,target):
    if guess < target:
        return 'too low'
    elif guess == target:
        return 'correct'
    else:
        return 'too high'

/*Q-10: Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and 
a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. 
If we are on vacation and it is a weekend (0 - Saturday or 6 - Sunday) it should return "off" and otherwise return "10:00". 
If we are not on vacation and it is a weekend it should return "10:00" and otherwise "7:00"*/
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

/*Q-11: The following code should create two functions. 
First create a function called square_it, which squares the parameter n and returns the result. 
Then, create a function called cube_it which cubes the parameter n and returns the result. 
Then ask the user to input a number. Lastly, print out the user's input squared and then cubed.*/
def square_it(n):
    return n * n
def cube_it(n):
    return n * n * n
a_num = int(input("Please enter a number"))
print(square_it(a_num))
print(cube_it(a_num))

/*Q-12: The following code creates three functions that calculate geometric equations. 
First create a function called distance, which finds and returns the distance between two coordinates, using the distance formula where d = √((x_2-x_1)²+(y_2-y_1)²). 
Then, create a function called area, which returns the area of a circle given the radius, using the formula A = πr². 
Finally, create a function called area2, which uses the previous two functions to return the area of a given circle. 
Remember that ** is exponent notation in Python and watch your indentation!*/

def distance(x1, y1, x2, y2):
     dx = x2 - x1
     dy = y2 - y1
     dsqured = dx**2 + dy**2
     result = dsquared**0.5
     return result
 def area(radius):
     b = 3.14159 * radius**2
     return b
 def area2(xc, yc, xp, yp):
     radius = distance(xc, yc, xp, yp)
     result2 = area(radius)
     return results2





