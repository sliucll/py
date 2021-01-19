#1 Find sequences with one uppercase letter followed by an underscore followed by one or more lowercase letters.
import re
def text_match(text):
    pattern = '[A-Z]_[a-z]+'
    if re.search(pattern,  text):
            return('Found a match!')
    else:
            return('Not matched!')

print(text_match("aab_cbbbc"))

#2 Check if a string begins with a word character. If it does, return “Found a match!”, if not return “Not matched!” 
import re
def text_match(text):
    pattern = '^\w'    
    if re.search(pattern, text):
        return('Found a match!')
    else:
        return('Not matched!')
print(text_match("The quick brown fox jumps over the lazy dog."))
