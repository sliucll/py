#Q-1 Construct a block of code that sorts the string 'txt' into a list of tuples (the first element is the length of the word, the second is the word itself). 
#Sort the list in terms of word length from longest to shortest.
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = []
for word in words:
    t.append((len(word),word))
t.sort(reverse = True)
print(t)
