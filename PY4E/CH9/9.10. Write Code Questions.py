#1. Write a program that categorizes each mail message by which day of the week the commit was done. 
#To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
#At the end of the program print out the contents of the dictionary ‘mail_count’ (order does not matter).
mail = ['From stephen.marquard@uct.ac.za Sat Jan  7', 'From gopal.ramasammycook@gmail.com Thurs Jan  5', 'From louis@media.berkeley.edu Tues Jan  3', 'From antranig@caret.cam.ac.uk Sat Jan  7', 'From david.horwitz@uct.ac.za Wed Jan  4', 'From ray@media.berkeley.edu Mon Jan  2', 'From stephen.marquard@uct.ac.za Mon Jan 2', 'From wagnermr@iupui.edu Fri Jan  6']

# Create dictionary for the emails
mail_count = {}

# Iterate through each email in the list
for email in mail:
    # Separate pieces of each email setting key to the day (third element)
    day = email.split()[2]
    print(email.split())
    print(day)
    # Add key to dictionary if not included
    if day not in mail_count.keys():
        mail_count[day] = 0
    # Update key
    mail_count[day] = mail_count[day] + 1
# Print final count
print(mail_count)

#2. Write a program to read through a mail log, 
#build a histogram using the dictionary “user_count” to count how many messages have come from each email address, and print the dictionary.
mail_log = ['From stephen.marquard@uct.ac.za Sat Jan  7', 'From gopal.ramasammycook@gmail.com Thurs Jan  5', 'From stephen.marquard@uct.ac.za Sat Feb  7', 'From louis@media.berkeley.edu Tues Jan  3', 'From stephen.marquard@uct.ac.za Sat Nov  6', 'From antranig@caret.cam.ac.uk Sat Jan  7', 'From david.horwitz@uct.ac.za Wed Jan  4', 'From ray@media.berkeley.edu Mon Jan  2', 'From stephen.marquard@uct.ac.za Mon Jan 2', 'From wagnermr@iupui.edu Fri Jan  6', 'From gopal.ramasammycook@gmail.com Thurs Dec  5', 'From louis@media.berkeley.edu Tues April  1']

user_count = dict()

for line in mail_log:
    mail = line.split()[1]
    if mail not in user_count.keys():
        user_count[mail] = 0
    user_count[mail] += 1
    
print(user_count)

#3. Write a program that creates a dictionary letter_count that keeps track of the amount of times each letter appears in the given phrase. 
#Assign the number of times “e” appears in the phrase to the variable “e_counter”. Make sure to account for each letter in its lowercase form.
# Create dictionary for letters and their counts
letter_count = {}

# Iterate through words in string
for word in phrase.split():
    # Iterate through each letter
    for letter in word:
        # Put each letter into lowercase
        letter = letter.lower()
        # Add letter as key to dictionary, if not included
        if letter not in letter_count.keys():
            letter_count[letter] = 0
        # Update letter
        letter_count[letter] += 1
# Create e_counter to see how many are in the phrase
e_counter = letter_count['e']

#4. Write a program that reads the words in the string ‘phrase’ and counts how many times each word appears. 
#Store the words as keys in the dictionary ‘word_dictionary’, then use the in operator as a fast way to check whether the string is in the dictionary.
phrase = "Writing programs or programming is a very creative and rewarding activity  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem  This book assumes that {\em everyone} needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills"

word_dictionary = dict()

#import re
#nw_phrase = re.sub(r'[^\w]',' ',phrase)

for word in phrase.split():
    if word not in word_dictionary.keys():
        word_dictionary[word] = 0
    word_dictionary[word] +=1

print(word_dictionary)

#5. Write code that reads in the text from the file words.txt, and uses the dictionary ‘word_count’ to count the amount of times a word appears in the file. 
#Watch out for repetition using the .lower() function.

# Open the file in "read" mode
with open("words.txt", "r") as filename:
    # Create dictionary to count words
    word_count = {}
    # Separate lines and iterate through them
    lines = filename.readlines()
    for line in lines:
        # Iterate through each word
        for word in line.split():
            # Set each word to lowercase
            word = word.lower()
            # Add word to dictionary if not included
            if word not in word_count.keys():
                word_count[word] = 0
            # Update word
            word_count[word] += 1
# Print final count
print(word_count)

#6.Perform the same task as in question 4, but this time make sure to look at words in lowercase in order to avoid any repetition.

phrase = "Writing programs or programming is a very creative and rewarding activity  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem  This book assumes that {\em everyone} needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills"

word_dictionary = dict()

#import re
#nw_phrase = re.sub(r'[^\w]',' ',phrase)

for word in phrase.split():
    if word not in word_dictionary.keys():
        word = word.lower()
        word_dictionary[word] = 0
    word_dictionary[word] +=1

print(word_dictionary)

#7. Write code that adds the key ‘two’ with a value of ‘dos’ to the dictionary eng2sp.
eng2sp = {'one':'uno'}
eng2sp['two'] = 'dos'

#8. Add code to the program below to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, 
#look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) 
#to find who has the most messages and print how many messages the person has.
# Open file in read mode
with open("mbox-short.txt3", "r") as filename:
    # Create message_count dictionary
    message_count = {}
    # Create variable for lines of the file
    messages = filename.readlines()
    # Iterate through each message (each line)
    for message in messages:
        # Assign the key to the first (0th) element of the message
        key = message.split()[0]
        # Assign the value to the second element of the message
        value = message.split()[1]
        # Check if key is already in dictionary
        if key not in message_count.keys():
            # if not, add key/value pair to dictionary
            message_count[key] = value
# Create variable to count emails
max_emails = 0
# Iterate through keys in dictionary
for key in message_count.keys():
    # Check if key is larger than the max emails
    if int(message_count[key]) >= max_emails:
        # If so, reassign max_emails to that key
        max_emails = int(message_count[key])
print(max_emails)

#9. Write this program to record the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). 
#At the end of the program, print out the contents of your dictionary.
with open("mbox-short.txt2", "r") as filename:
    message_count = {}
    lines = filename.readlines()
    #print(lines)
    for line in lines:
        line = line.split()
        key = line[0]
        host_pos = key.find('@')
        host = key[host_pos+1:]
        value = line[1]
        #print(host,value)
        if host not in message_count.keys():
            message_count[host] = value
    print(message_count)
