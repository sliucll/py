#1. It prints “Hi”
s1 = "hi"
s1 = s1.capitalize()
print(s1)

#2. Only “meow” is printed.
sentence = "The cat goes meow."
s2 = sentence[13:17]
print(s2)

#3. Write the code to evaluate the length of the string “I like green eggs” and print it. It should print “The length is 17”.
phrase = "I like green eggs"
length_string = len(phrase)
print("The length is",str(length_string))

#4. Create a function named count that accepts a string and a letter as arguments, then returns the count of that letter in the string. 
#For example, if the function call was count("banana", "a") it would return 3.
def count(text, aChar):
    count = 0
    for c in text:
        if c == aChar:
            count = count + 1
    return count

count("banana", "a")

#5. Take the following Python code that stores this string: string = "X-DSPAM-Confidence: 0.8475". 
#Use find and string slicing to extract the portion of the string after the colon character and 
#then use the float function to convert the extracted string into a floating point number called num.
string = "X-DSPAM-Confidence: 0.8475"
col_pos = string.find(':')
pos = col_pos + 1
num = float(string[pos:])
print(num)

#6. In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. 
#ALT1
prefixes = 'JKLMNOPQ' 
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':  # if the letter is O or Q
        print letter + 'u' + suffix
    else:
        print letter + suffix

#ALT2
prefixes = ["J","K","L","M","N","Ou","P","Qu"]
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)
    
#7. Write a function numDigits that will return the number of digits in an integer n.
def numDigits(n):
    n_str = str(n)
    return len(n_str)

# Check the function
print(numDigits(50))
print(numDigits(20000))
print(numDigits(1))

#8. Write code to print out the statement “Hi, my name is Bob, and I am 2” using only string methods or string slicing. 
#You must get every part of the new string from the given strings. Name the final string statement.
s1 = "hi"
s2 = "My name is Bob, and he and I love to eat ham."
s1 = s1.capitalize()
comma = s2[s2.find(','):s2.find('and')]
print(comma)
name_intro = s2[s2.find('My'):s2.find('he')]
name_intro = name_intro[0].lower() + name_intro[1:] 
print(name_intro)
age_intro = s2[s2.find('I'):s2.find('love')]
age_intro_verb = s2[(s2.find('ham')+1):-1]
age = len(s1)
print(age)

statement = s1 + comma + name_intro + age_intro + age_intro_verb + " " + str(age)
print(statement)

#9. Write a program that asks a user for their name and from the input prints the first letter of their name in lowercase.
prompt = "What is your name?"
name = input(prompt)
first = name[0]
lowerFirst = first.lower()
print(lowerFirst)

#10. Write a program that asks for user input and prints their input in all lowercase, as well as the length of their string.
name = input("What is your name?\n")
name_1st_lw = name.lower() 
length = len(name_1st_lw)
print("Your name in lower case:",name_1st_lw)
print("Your name's length:",length)
