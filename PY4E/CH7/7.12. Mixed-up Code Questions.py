#Q-1: The following program should open a file, write a line, and close the file
fout = open('output.txt','w')
file.write("This here's the wattle,\n")
fout.close()

#Q-2: The following program counts the number of characters in the file "travel_plans.txt"
First create a variable num and initialize it. Then open the file. 
Loop reading a line from the file and add the length of each line to num. Then print the result.
num = 0
travelFile = open("travel_plans.txt", "r")
for line in travelFile:
    num = num + len(line)
print(num)

#Q-3: The following program writes the squares of some numbers to the file "squared_numbers.txt". 
outfile = open("squared_numbers.txt","w")
for number in range(1,13):
    square = number * number
    outfile.write(str(square) + "\n")
outfile.close()

#Q-4: The following program should split the lines of "olympics.txt", then print the name, team, and event of each athlete in a sentence. 
olympicsfile = open("olympics.txt","r")
for line in olympicsfile:
    values = line.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()

#Q-5: The following program prints the pollution information for all cities that start with a ``D``
# open the file for reading
inFile = open("uspoll.txt","r")
# while there is another line
for line in inFile:
    #split at the :
    v = line.split(":")
    #get the city
    city = v[0]
    #if city starts with an D print info
    if (city.find("D") == 0):
        print("City: ",city)
        print("Pollution values:",v[1],v[2])
#close the file
inFile.close()

# Q-6: PM 2.5 is an air pollutant that is harmful at high levels. The following program prints the maximum PM 2.5 pollution found
# read all the lines
infile = open("uspoll.txt","r")
lines = infile.readlines()
infile.close()
#initialize the variables
maxCity = ''
max25 = 0
#loop through the lines
for line in lines:
    #split at:
    values = line.split(":")
    #get the PM 2.5 pollution
    new25 = float(values[2])
    #if current > max
    if new25 > max25:
        #save the new max info
        maxCity = values[0]
        max25 = new25
#print the largest PM 2.5 values
print("Largest is ",max25," in ",maxCity)

#Q-7: The following program prints the minimum PM 2.5 pollution found
infile = open("uspoll.txt","r")
lines = infile.readlines()
infile.close()
#initialize the variables
minCity = ''
min25 = 500
#loop through the lines
for line in lines:
    #split at:
    values = line.split(":")
    #get the PM 2.5 pollution
    new25 = float(values[2])
    #if current > max
    if new25 > min25:
        #save the new max info
        minCity = values[0]
        max25 = new25
#print the largest PM 2.5 values
print("Smallest PM 2.5 ",min25," in ",minCity)

#Q-8: The following program prints the average PM 2.5 pollution found
infile = open("uspoll.txt","r")
lines = infile.readlines()
infile.close()
#initialize the variables
total25 = 0
count = 1.0
#loop through the lines
for line in lines:
    #split at:
    values = line.split(":")
    #get the PM 2.5 pollution
    new25 = float(values[2])
    #add to thte total and count
    total25 = total25 + new25
    count = count + 1
#print the average PM 2.5 values
print("Average PM 2.5 value is",total25/count)

#Q-9: The following program prints the average PM 2.5 pollution for a state
# read all the lines
infile = open("uspoll.txt","r")
lines = infile.readlines()
infile.close()
#initialize the variables
state = "CA"
total25= 0
count = 1.00
#loop through the lines
for line in lines:
    #split at :
    values = line.split(":")
    #split at ,
    cityState = values[0].split(",")
    #if found state
    if cityState[1].find(state) >= 0:
        #add the current to the sum
        new25 = float(values[2])
        total25 = total25 + new25
        #increment the count
        count = count + 1
#print the average
avg = total25/count
print("Avg for ", state, " is ", avg)
