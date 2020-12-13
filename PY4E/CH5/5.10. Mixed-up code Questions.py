#Q-1: The following program segment should, as long as n is less than 5, print n and then increment it by 1. 
n = 0
while n < 5:
    print(n)
    n = n + 1
    
#Q-2: The following program segment should print "0 2 4 6" on separate lines by using a while loop. 
Arrange the code so that "accum" prints before increasing its value.
accum = 0
while accum < 7:
    print(accum)
    accum = accum + 2
    
#Q-3: The following program segment should print all even numbers from 0 to 8 (this includes 0 and 8).
def skipCount(start, increment, stop):
    counter = start
    while counter < stop:
        print(counter)
        counter = counter + increment
    return counter

skipCount(0,2,9)

#Q-4: The following program segment should infinitely loop.
def loopMe(first,second):
    while first > second:
        print('Am I infinitely looping?')
    return True

loopMe(7,4)

#Q-5: The following program segment should calculate and print the average of a list of numbers using a for loop. 
numbers = [90,94,85,78,87,98]
sum = 0
for number in numbers:
    sum = sum + number
print(sum/6)

#Q-6: The following program segment should calculate and print the sum of all numbers between 0 and 30.
#By default, two arguments i.e., start = 0, stop = 30, step = 1
sum = 0
numbers = range(31)
for number in numbers:
    sum = sum + number
print(sum)

#Q-7: The following program segment should calculate the sum of all odd numbers between 0 and 30. 
#Three arguments i.e., start = 1, stop = 30, step = 2.
sum = 0
numbers = range(1,30,2)
for number in numbers:
    sum = sum + number
print(sum)

#Q-8: The following program should find the sum of every multiple of 3 between 3 and 36 and print the sum after each addition. 
sum = 0
numbers = range(3,37,3)
for number in numbers:
    sum = sum + number
    print(sum)
    
#Q-9: The following program should find the average pH of 6 water samples. 
total = 0
pHvalues = [7.0, 8.2, 6.7, 7.5, 8.0, 7.2]
for number in pHvalues:
    total = total + number
average = total / 6
print(average)

#Q-10: The following program should print the numbers 5 through 1, starting with 5. 
counter = 5
while counter > 0:
    print(counter)
    counter = counter - 1
