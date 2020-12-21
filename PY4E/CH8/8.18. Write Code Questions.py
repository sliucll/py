#1. Fix the 5 syntax errors in the code below so that it runs. It should print the length of myFirstList and print the result of myFirstList * 3. 
#Then it should set mySecondList to the concatenation of myFirstList and a list containing 321.4. 
#Then it should print the value of mySecondList.
myFirstList = [12,"ape",13]
print(len(myFirstList))
print(myFirstList * 3)
mySecondList = myFirstList + [321.4]
print(mySecondList)

#2. It runs and prints the contents of items.
def itemLister(items):
    items[0] = "First item"
    items[1] = items[0]
    items[2] = items[2] + 1
    print(items)

itemLister([2,4,68])

#3. The function returns the average of a list of integers.
def gradeAverage(aList):
    sum = 0
    for num in aList:
        sum = num + sum
    average = sum/len(aList)
    return average

aList = [99, 100, 74, 63, 100, 100]
print(gradeAverage(aList))

#4. Assign the value of the item at index 3 of l to “200”
l = ["hi", "goodbye", "python", "106", "506"]
l[3] = "200"
print(l)

#5. Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []],[['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
data_last = data[-1]
print(data_last)
plant = data_last[0][0]
print(plant)

#6. Write a function called countWords that returns a count of how many words in the pased list, lst, have length 5.
def countWords(lst):
    count = 0
    for word in lst:
        if len(word) == 5:
            count = count + 1
    return count

#7. Write a function called chop that takes a list lst and modifies it, removing the first and last elements.
def chop(lst):
    del lst[0]
    del lst[-1]
    return(lst)

#8. see #7

#9. Sum all the elements in the list lst up to but not including the first even number.
def sumUntilEven(lst):
    total = 0
    element = 0
    while element < len(lst) and lst[element] % 2 != 0:
        total = total + lst[element]
        print("tot:",total)
        element = element + 1
        print("ele:",element)
    return total

sumUntilEven([1,3,5,7,9])

#10. Write a function called reverse that returns the reverse of a passed list.
def reverse(lst):
    lst.reverse()
    return lst
