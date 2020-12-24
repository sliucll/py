#1. Write a program that categorizes each mail message by which day of the week the commit was done. 
#To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
#At the end of the program print out the contents of the dictionary ‘mail_count’ (order does not matter).
mail = ['From stephen.marquard@uct.ac.za Sat Jan  7', 'From gopal.ramasammycook@gmail.com Thurs Jan  5', 'From louis@media.berkeley.edu Tues Jan  3', 'From antranig@caret.cam.ac.uk Sat Jan  7', 'From david.horwitz@uct.ac.za Wed Jan  4', 'From ray@media.berkeley.edu Mon Jan  2', 'From stephen.marquard@uct.ac.za Mon Jan 2', 'From wagnermr@iupui.edu Fri Jan  6']

# Create dictionary for the emails
mail_count = {}

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

#1. Write a program to read through a mail log, 
#build a histogram using the dictionary “user_count” to count how many messages have come from each email address, and print the dictionary.
