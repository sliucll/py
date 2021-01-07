#1. Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.
tup1 = ('a', 'b', 'c')

#2. Provided is a list of tuples. Create another list called t_check that contains the third element of each tuple.
lst_tups = [('Articuno', 'Moltres', 'Zapdos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", 'Tauros', 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Seviper', 'Wailord', 'Sealeo')]

t_check = []
for i in lst_tups:
    items = i[2]
    t_check.append(items)
    
print(t_check)

#3. The dictionary ‘majors’ contains college major codes as keys and college major names as values. 
#Write a function named find_major() that takes one parameter, a major code. 
#If the major code exists in ‘majors’, your function should return a tuple where the first value is the major code and the second is the name of the major. 
#If the major code doesn’t exist, return a tuple where the first value is None and the second is a string containing ‘Error’. 
#Finally, test your function by printing the name of the major with code 3084.
majors = {3084: 'Computer Science', 3025: 'Electrical Engineering', 3020: 'Computer Engineering', 3027: 'Cybersecurity', 3068: 'Biometric Systems Engineering'}
# Define find_major function with one parameter
def find_major(major_code):
    # if the parameter is in the keys of the dictionary above
    if major_code in majors.keys():
        # return the parameter and the name from the dictionary
        return (major_code, majors[major_code])
    # Create an else statement
    else:
        # Return an error if not found
        return (None, 'Error')
# Test your function!
print(find_major(3084))

#4. Write code to interchange the values of tuple t.
t = ("LeBron", "James") 
t = t[::-1]

#5. If you remember, the items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. 
#For each key-value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the keys() or values() methods.
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = []
p_number = []
for key,val in pokemon.items():
    p_names.append(key)
    p_number.append(val)
    
print(p_names)
print(p_number)

#6. Create a tuple called my_data that contains one element, the integer 99.
my_data = (99,)

#7. Write code to print list_of_tuples where the last value of each tuple is 100. Assign this new list of tuples to the variable updated_list.
# Access the last element of each list (-1) and replace with 100 in each element of the tuple
updated_list = [tup[:-1] + (100,) for tup in list_of_tuples]
# print the updated list
print(updated_list)

#8. Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown. 
#The function should return a tuple that contains all the inputted information.
def info(name,age,birth_year,year_in_college,hometown):
    return (name,age,birth_year,year_in_college,hometown)

#9. Write a function list_link that accepts two lists and returns a dictionary with the first list as the key and the second list as the value. 
#For example, list_link(['what', 'do', 'you', 'do'], [1,2,3,4]) should return {'what': 1, 'do': 4, 'you': 3}.
def list_link(lst1,lst2):
    diction = {}
    counter = 0
    if len(lst1) == len(lst2):
        for i in lst1:
            diction[i] = lst2[counter]
            counter = counter + 1
    return diction

print(list_link(['what', 'do', 'you', 'do'], [1,2,3,4]))

#10. Create a function tuplize() that accepts two inputs and returns a tuple containing those inputs in order.
def tuplize(x,y):
    return (x,y)


