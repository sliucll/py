#1. Fix errors in the code below so that the code runs correctly and prints the pollution for all cities that start with the letter A.
# Close quotations around "r"
inFile = open("uspoll.txt","r")

# Add a colon at the end
for line in inFile:
    values = line.split(":")
    city = values[0]
    if (city.find("A") == 0):
        # "+" is needed to concatenate strings and variables
        print('City: ' + city)
        print("Pollution values:",values[1],values[2])

inFile.close()

#2. Fix the errors in the code below so that it prints the average PM values of only the cities that start with “A”.
inFile = open("uspoll.txt","r")
lines = inFile.readlines()
inFile.close()

total25 = 0
count = 1.0
for line in lines:
    values = line.split(":")
    new25 = float(values[2])
    city = values[0]
    if (city.find("A") == 0):
        print(city)
        total25 = total25 + new25
        count = count + 1

print("Average PM 2.5 value for cities that start with 'A' is ", total25/count)

#3. It prints out all lines that have a city that starts with “A” or “B”.
#ALT1
inFile = open("uspoll.txt","r")
lines = inFile.readlines()
inFile.close()

for line in lines:
    if line[0] == "A" or line[0] == "B":
        print(line)

#ALT2
# Read all the lines
inFile = open("uspoll.txt","r")
lines = inFile.readlines()
inFile.close()

# Loop through the lines
for line in lines:
    # Set condition for lines starting with A or B
    # Be sure to close parentheses to separate phrases
    if (line[0] == "A") | (line[0] == "B"):
        print(line)

#4. Print the lowest 2.5 value and city.
inFile = open("uspoll.txt","r")
lines = inFile.readlines()
inFile.close()

minCity = ''
min25 = 500
for line in lines:
    values = line.split(":")
    new25 = float(values[2])
    if new25 < min25:
        minCity = values[0]
        min25 = new25
print("Smallest PM 2.5 ",min25," in ",minCity)

#5. Using the text file studentdata.txt write a program that prints out the names of students that have six or more quiz scores.
data = open("studentdata.txt","r")
for line in data:
    clean = line.rstrip()
    values = clean.split(" ")
    #print(len(values))
    if len(values) >= 7:
        print(values[1:])
        print(values[0])
        
#6. 
