#Q-1: Write a program that will print out the length of each item in the list as well as the first and last characters of the item.
weather = ["sunny","cloudy","partially sunny","rainy","storming","windy","foggy","snowy","hailing"]
for condition in weather:
    print("The word is",len(condition),"characters")
    first_char = condition[0]
    last_char = condition[-1]
    print("The first character is: " + first_char)
    print("The last character is: " + last_char)

#Q-2: Let's imagine that you have a list that contains amounts of rainfall for each day, collected by a meteorologist. 
#Her rain gathering equipment occasionally makes a mistake and reports a negative amount for that day. 
#We have to ignore those. We need to write a program to 
#(a) calculate the total rainfall by adding up all the positive integers (and only the positive integers), 
#(b) count the number of positive integers (we will count with "1.0" so that our average can have a decimal point), and 
#(c) print out the average rainfall at the end. 
#Only print the average if there was some rainfall, otherwise print "No rain". 
#Construct a program that correctly solves the rainfall problem. 
rain = [0,5,1,0,-1,6,7,-2,0]
sumRain = 0
count = 0
for day in rain:
    if day >= 0:
        sumRain = sumRain + day
        count = count + 1.0
        print(count)
if count > 0:
    ave = sumRain / count
    print("Average",ave)
else:
    print("No rain")
    
#Q-3: The following program segment should swap the first and last values of the list "numbers" using indexing. 
numbers = [3,2,1,4]
first = numbers[0]
last = numbers[3]
numbers[0] = last
numbers[-1] = first

#Q-4: The following program segment should iterate through the list of prices and discount them by 50%.
price_lst = [21.99,25.99,19.99,10.99,15.99]
discounts = []

for price in price_lst:
    new_price = price*0.50
    discounts.append(new_price)

print(discounts)

#Q-5: The following program segment should iterate through the strings in list and append them to long_list if the length is greater than 4.
list = ["four","Michigan","yellow","at","blue"]
long_list = []
for item in list:
    if len(item) > 4:
        long_list.append(item)

print(long_list)

#Q-6: The following program segment should first replace the last item of the list months with "November" then append "December" to the end of the list.
months = ["Janurary","March","June","August","October"]
new_month = "November"
months[4] = new_month
months.append("December")
print(months)

#Q-7: The following program segment should iterate through the list terms and then add each item to the list vocab if it is not already in the list. 
#If the word is already in vocab, then the program should add 1 to the variable "counter". 
terms = ["accent","vertigo","libra","illusion"]
vocab = ["hereditary","illusion","vertigo","velocity","fallacy"]
counter = 0
for word in terms:
    if word NOT in vocab:
        vocab.append(word)
        print(vocab)
    elif word in vocab:
        counter += 1
        print(counter)

#Q-8: The following program segment should reverse the order of the list oldList, by storing it in the list newList.
oldList = ["this","is","a","list"]
newList = []
for x in range(0, len(oldList)):
    newList = oldList[x] + newList
print(newList)

#Q-9: The following program segment should first print out the program's instructions. 
#Next it should continuously ask the user if it wants to add a word to a list vocabulary and then append it to the end the list IF the word is not already in the list. 
print("Enter a word to add it to the vocabulary list or type in 'quit' to end the program.")
response = 0
vocabulary = []
while response != "quit":
    response = input("Enter a vocabulary word:")
    if response not in vocabulary:
        vocabulary.append(response)
        print(vocabulary)
  
print(vocabulary)

#Q-10: The following program should create a definition countOdd that takes in a list as its argument and returns how many odd numbers are in the list.
def countOdd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd

