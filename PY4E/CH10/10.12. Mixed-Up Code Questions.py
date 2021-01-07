#Q-1 Construct a block of code that sorts the string 'txt' into a list of tuples (the first element is the length of the word, the second is the word itself). 
#Sort the list in terms of word length from longest to shortest.
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = []
for word in words:
    t.append((len(word),word))
t.sort(reverse = True)
print(t)

#Q-2 Reorder the blocks of code to create a list containing tuples of each word from word_list paired with their lengths. Then sort the words by length from highest to lowest.
word_list = ['pen','skyscraper','post','computer','apple','Hollywood']
tup_list = []
for word in word_list:
    tup = word, len(word)
    print(tup)
    tup_list.append(tup)
    print(tup_list)
tup_list.sort(key = lambda x: x[1], reverse = True)
print("Sorted tup list:",tup_list)
#output
('pen', 3)
[('pen', 3)]
('skyscraper', 10)
[('pen', 3), ('skyscraper', 10)]
('post', 4)
[('pen', 3), ('skyscraper', 10), ('post', 4)]
('computer', 8)
[('pen', 3), ('skyscraper', 10), ('post', 4), ('computer', 8)]
('apple', 5)
[('pen', 3), ('skyscraper', 10), ('post', 4), ('computer', 8), ('apple', 5)]
('Hollywood', 9)
[('pen', 3), ('skyscraper', 10), ('post', 4), ('computer', 8), ('apple', 5), ('Hollywood', 9)]
Sorted tup list: [('skyscraper', 10), ('Hollywood', 9), ('computer', 8), ('apple', 5), ('post', 4), ('pen', 3)]
    
#Q-3 Construct a block of code that swaps the second and fourth values of tuple t with one another.
t = ('Apple','Banana','Grapefruit','Pear','Peach')
a,b,c,d,e = t
t = a,d,c,b,e
print(t)

#Q-4 Reorder the blocks of code to transform the dictionary 'd' into a list of tuples called tup_list, and sort it by the dictionary's keys in ascending order.
d = {'a':10,'b':2,'c':27,'d':15,'e':30,'f':3}
tup_list = list(d.items())
tup_list.sort()
print(tup_list)

#Q-5 Construct a block of code that uses tuples to keep track of the word count in the file 'heineken.txt'. Then print out the 10 most frequently occurring words from the file.
word_counter = {}
with open("heineken.txt","r") as filename:
    lines = filename.readlines()
    for line in lines.split():
        for word in line:
            word_counter[word] = word_counter.get(word,0) + 1
    list_of_tuples = list(word_counter.items())
    list_of_tuples.sort(key = lambda x: x[1], reverse = True)
    for i in range(10):
        print(list_of_tuples[i][0])
        
#Q-6 Construct a block of code to add the key-value pairs of dictionary d to a list and then print them.
d = {'monkey':5,'snake':3,'rabbit':9,'dragon':6,'rooster':2,'rat':10}
list_for_kv_pairs = []
for key,val in d.items():
    print(key,val)
    list_for_kv_pairs.append((key,val))
print(list_for_kv_pairs)

#Q-7 Reorder the code blocks to put the words in the mbox-short.txt file into a dictionary, where the keys are words and the values are their lengths. 
#Then, print a list of the dictionary's key-value pairs in alphabetical order.
