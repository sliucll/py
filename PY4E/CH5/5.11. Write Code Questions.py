#1. print a countdown of the numbers from 10 to 0
def countdown():
    counter = 10
    # Keep running loop until counter equals 0 
    # Use correct variable name (counter is lowercase)
    while counter >= 0:
        # Keyword print is lowercase
        print(counter)
        # Decrement to lower the counter
        counter = counter - 1
# Call correct function name (countdown)
countdown()

#2. Make the loop only have five iterations.
x = 5
while x < 10:
    print(x)
    x = x + 1
    
#3. Print a count up from -10 to 0, including 0.
output = ""
# Start x at -11 so it stays under 0
x = -11
# First line of a loop ends with a colon (:)
while x < 0:
    # Since the iteration variable is negative, increase the count
    x = x + 1
    # Output reassignment is within the loop
    output = output + str(x) + " "
# Close print parentheses
print(output)

#4. Prints every integer from -5 to -1, including -1.
output = ""
x = -6
while x < -1:
    x = x + 1
    output = output + str(x) + " "
print(output)

#5. Prints the number 6. (N.B. the loop stops until the "while" condition has been fulfilled.)
x = 3
i = 0
while i < 3:
    # Increase x by 1 for each run of the loop
    x = x + 1
    i = i + 1
# Print the x variable
print(x)

#6. Print an estimate of the square root of a number.
target = 6
guess = 2
guessSquared = guess * guess
while abs(target-guessSquared) > 0.01:
    closer = target / guess
    guess = (guess + closer) / 2.0
    guessSquared = guess * guess
print("Square root of", target, "is", guess)

#7. Change the for loop to a while loop while still using the same parameters.
def sumFunc(start, stop):
    sum = 0
    for num in range(start, stop + 1):
        sum = sum + num
    return sum

print(sumFunc(1,10))

def sumFunc(start, stop):
    sum = 0
    # Create an iteration variable, initialized to the start argument
    num = start
    # Use while loop until iteration variable is less than or equal to stop argument
    while num <= stop:
        # Add number to sum
        sum = sum + num
        # Increase iteration variable
        num = num + 1
    # Return the sum
    return sum

print(sumFunc(1,10))

#8. The program below is supposed to print the times tables from 1 to 3, but there are 5 errors.
for x in range(1,4):
     for y in range(1,4):
         print(str(x) + " * " + str(y) + " = " + str(x*y))

#9. Use a while and a for loop instead of 2 for loops.
for x in range(1, 4):
    for y in range(1, 4):
        print(str(x) + " * " + str(y) + " = " + str(x * y))

for x in range(1, 4):
    # Create an iteration variable, starting in the range
    y = 1
    # Use while loop if the iteration variable is less than 4
    while y < 4:
        # Print the string
        print(str(x) + " * " + str(y) + " = " + str(x * y))
        # Increment the iteration variable
        y = y + 1
        
#10. Rewrite the following code to use a while loop instead of a for loop.
product = 1  # Start out with nothing
numbers = range(1,11)
for number in numbers:
    product = product * number
print(product)

product = 1  # Start out with nothing
numbers = 1
while numbers < 11:
    product = product * numbers
    numbers = numbers + 1
print(product)
