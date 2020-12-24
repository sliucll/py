#Q-1: Construct a block of code that prints a dictionary containing the amount of times a letter appears in the given string.
phrase = 'Explore the NEW Wolverine Access'
d = dict()
for word in phrase:
    for letter in word.lower():
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
print(d)

"""if letter not in d: d[letter] = 1"""
{'e': 1}
{'e': 1, 'x': 1}
{'e': 1, 'x': 1, 'p': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1, 'v': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1, 'v': 1, 'i': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1, 'v': 1, 'i': 1, 'a': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1, 'v': 1, 'i': 1, 'a': 1, 'c': 1}
{'e': 1, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1, 'n': 1, 'w': 1, 'v': 1, 'i': 1, 'a': 1, 'c': 1, 's': 1}

"""else: d[letter] += 1"""
{'e': 2, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1}
{'e': 3, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 1, 't': 1, 'h': 1}
{'e': 3, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 2, 't': 1, 'h': 1}
{'e': 4, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 2, 't': 1, 'h': 1, 'n': 1}
{'e': 4, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 3, 't': 1, 'h': 1, 'n': 1, 'w': 1}
{'e': 4, 'x': 1, 'p': 1, 'l': 1, 'o': 1, 'r': 1, ' ': 3, 't': 1, 'h': 1, 'n': 1, 'w': 2}
{'e': 4, 'x': 1, 'p': 1, 'l': 1, 'o': 2, 'r': 1, ' ': 3, 't': 1, 'h': 1, 'n': 1, 'w': 2}
{'e': 4, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 1, ' ': 3, 't': 1, 'h': 1, 'n': 1, 'w': 2}
{'e': 5, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 1, ' ': 3, 't': 1, 'h': 1, 'n': 1, 'w': 2, 'v': 1}
{'e': 5, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 3, 't': 1, 'h': 1, 'n': 1, 'w': 2, 'v': 1}
{'e': 5, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 3, 't': 1, 'h': 1, 'n': 2, 'w': 2, 'v': 1, 'i': 1}
{'e': 6, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 3, 't': 1, 'h': 1, 'n': 2, 'w': 2, 'v': 1, 'i': 1}
{'e': 6, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 4, 't': 1, 'h': 1, 'n': 2, 'w': 2, 'v': 1, 'i': 1}
{'e': 6, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 4, 't': 1, 'h': 1, 'n': 2, 'w': 2, 'v': 1, 'i': 1, 'a': 1, 'c': 2}
{'e': 7, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 4, 't': 1, 'h': 1, 'n': 2, 'w': 2, 'v': 1, 'i': 1, 'a': 1, 'c': 2}
{'e': 7, 'x': 1, 'p': 1, 'l': 2, 'o': 2, 'r': 2, ' ': 4, 't': 1, 'h': 1, 'n': 2, 'w': 2, 'v': 1, 'i': 1, 'a': 1, 'c': 2, 's': 2}

#Q-2: Construct a block of code that prints a dictionary containing the amount of times a word appears in the given string.
phrase = 'Explore the NEW Wolverine Access'
word_count = {}
for word in phrase.split():
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
print(word_count)

#if word not in word_count: word_count[word] = 0
{'Explore': 0}
{'Explore': 0, 'the': 0}
{'Explore': 0, 'the': 0, 'NEW': 0}
{'Explore': 0, 'the': 0, 'NEW': 0, 'Wolverine': 0}
{'Explore': 0, 'the': 0, 'NEW': 0, 'Wolverine': 0, 'Access': 0}

#word_count[word] + = 1 
{'Explore': 1}
{'Explore': 1, 'the': 1}
{'Explore': 1, 'the': 1, 'NEW': 1}
{'Explore': 1, 'the': 1, 'NEW': 1, 'Wolverine': 1}
{'Explore': 1, 'the': 1, 'NEW': 1, 'Wolverine': 1, 'Access': 1}

#Q-3: Rearrange the code blocks to make the code print out the amount of a's in the given phrase.
phrase = "Alice in Wonderland"
letter_counter = {}
for character in phrase: #print letter by letter in each word incl. spaces
    #print(character) 
    if character not in letter_counter.keys():
        letter_counter[character] = 0 #assign a default value "0" to each letter
        #print(letter_counter) 
    letter_counter[character] += 1 #add a value "1" to each default value
    print(letter_counter) 
print(letter_counter['a'])

#Q-4: Construct a block of code that correctly reads in a file, and counts the amount of times each word appears in the file.
with open("words.txt","r") as filename:
    word_counter = {}
    lines = filename.readlines()
    for line in lines:
        for word in line.split():
            if word not in word_counter.keys():
                word_counter[word] = 0
            word_counter[word] += 1
 
#Q-5: Place the code in the correct order so that the dictionary and key-value pairs are initialized/updated correctly.
temp_dictionary = dict()
temp_dictionary['barbell'] = 5
temp_dictionary['pull-up'] = 15
temp_dictionary['barbell'] += 10
temp_dictionary['pull-up'] *= 2

#Q-6: Construct a code block to transform the lists 'keys' and 'values' into one dictionary. Make sure to print the dictionary once the loop terminates.
keys = ['Ten','Twenty','Thirty']
print(len(keys))
values = [10,20,30]
combination = dict()
for i in range(len(keys)):
    print(i)
    if keys[i] not in combination.keys():
        print(keys[i])
        print(combination.keys())
        combination[keys[i]]  = values[i]
        print("ki:",keys[i],"vi:",values[i])
print(combination)

#Q-7: Rearrange the code blocks so the code prints the key containing the lowest value of all the keys in the dictionary.
sampleDict = {'Physics':82,'Math':65,'History':75}
sampleDict['English'] = 66
sampleDict['Ceramics'] = 90
sampleDict['History'] = 64
minimum_value = min(sampleDict.keys(),key=(lambda k: sampleDict[k]))
print(minimum_value,sampleDict[minimum_value])

#Q-8: Construct a code block to combine the key-value pairs of two dictionaries into one dictionary.
dict1 = {'Ten':10,'Twenty':20,'Thirty':30}
dict2 = {'Thirty':30,'Fourty':40,'Fifty':50}
dict3 = {}
print(dict1.keys())
for key in dict1.keys():
    #print("key:",key)
    if key not in dict3.keys():
        dict3[key] = dict1[key]
        print(key,dict3[key])
for key in dict2.keys():
    if key in dict3.keys():
        dict3[key] += dict2[key]
        print(key,dict3[key])
    else:
        dict3[key] = dict2[key]
 
#Q-9: Rearrange the following code blocks to figure out how much the items in grocery_dict will cost. Print the final total at the end of the code.
grocery_dict = {'apples':17,'oranges':3,'pears':10,'cucumbers':5,'avocados':2}
price_dict = {'apples':1.5,'oranges':1.25,'pears':1.5,'cucumbers':2,'avocados':2}
total_price = 0
for item in grocery_dict:
    price_of_item = price_dict[item] * grocery_dict[item]
    total_price += price_of_item
print(total_price)

#Q-10: Place the code in the correct order so it properly counts the amount of characters in a sentence using the .get() method.
sentence = "The quick brown fox jumped over the lazy dog"
characters = {}
for character in sentence:
    #print(character)
    characters[character] = characters.get(character,0) + 1
    print(character,characters[character])
print(characters)

