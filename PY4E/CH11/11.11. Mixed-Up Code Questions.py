#1 The following code should use regular expressions to find and print the phrase "Good morning!" from the list "greetings", if it is included in the list. 
import re
greetings = ["Hello!","hello.","Good Morning!","good morning!","Good morning!","hi"]
for item in greetings:
  if re.search('Good morning!',item):
    print(item)
    
#2 The following code should use regular expressions to print each item in the list "greetings", if it starts with an "H" or an "h". 
import re
greetings = ["Hello!","hello.","Good Morning!","good morning!","Good morning!","hi"]
for item in greetings:
  if re.search('^[Hh]',item):
    print(item)
    
#3 The following code should use regular expressions to print each item in the list "greetings", if it includes an "o".
import re
greetings = ["Hello!","hello.","Good Morning!","good morning!","Good morning!","hi"]
for item in greetings:
  if re.search('o',item):
    print(item)
    
#4 he following code should use create a regular expression pattern for the word "Puppy" and test it on the sequence. 
#If they are the same, it should print "Match!", if not it should print "Not a match!".
import re
pattern = r"Puppy"
sequence = "Puppies"
if re.match(pattern,sequence):
  print("Match!")
else:
  print("Not a match!")

#5 The following code should use create a regular expression pattern that can match "Sincerely, Molly" where there is at least one space after the comma, but can be many. 
#Test it on the sequence. If they are the same, it should print "Match!", if not it should print "Not a match!". 
import re
sequence = "Sincerely,        Molly"
pattern = r"Sincerely,\s+Molly"
if re.match(pattern, sequence):
  print("Match!")
else:
  print("Not a match!")
  
#6 The following code should create a new string "y" from the first price found in the string "x".
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$\d+(?:\.\d{2})?'.x)[0]

#7 The following code should read all the lines in a file, remove whitespace from the end of the line, and 
#use regular expressions to find and print out anything that looks like an email address.
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('\S+@\S+', line)
  for item in x:
    print(item)

#8 The following code should read all the lines in a file, remove whitespace from the right side of the line, and 
#use regular expressions to find and print out anything lines that start with “From:”, followed by one or more characters, followed by an at-sign. 
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('^From:.+@',line):
    print(line)

#9 The following code should read all the lines in a file, remove whitespace from the right side of the line, and 
#use regular expressions to search for lines that start with 'Details: rev=' followed by numbers and '.'. Then print the number of occurrences. 
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^Details:.*rev=([0-9]+\.)',line)
  print(len(x))
  
#10 The following code should search for lines that 
#start with 'X' followed by at least one non whitespace character then ':' followed by one space and at least one digit then print the number of items found. 
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^X\S+: [0-9]+',line)
  print(len(x))
