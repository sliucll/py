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

#2. 
