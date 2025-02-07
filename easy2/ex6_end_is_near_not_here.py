##### Problem statement

# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

############ PEDAC ###############

# inputs: input string of at least 2 words
# output: next to last word in string

# rules
# assume input string always contains at least 2 words
# words are any sequence of non-blank characters

# test cases
# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# data structure
# list returned by `split` method

# algorithm
# 1. Define function `penultimate` with a parameter of `words`
# 2. Within function, invoke `split` method on `words` and 
#    assign returned list to variable `words_list`
# 3. Return `words_list[-2]`

def penultimate(words):
    words_list = words.split()
    return words_list[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")