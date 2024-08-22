def data_request():
    word1 = input("Write the first word: ").lower()
    word2 = input("Write the second word: ").lower()
    return word1,word2

def anagram(anWord1,anWord2):
    #“sorted” sorts the word alphabetically
    sorted_word1 = sorted(anWord1) 
    sorted_word2 = sorted(anWord2)
    if sorted_word1 == sorted_word2:
        return print("We have a correct anagram")
    else: return print("Your words are not anagrams")

#Function call
"""
The return from data_resquest is a tuple, therefore, we assign this tuple in a variable, to be able to access its indexes
userWords[0] = is the user's first word, userWords[1] = is the user's second word
userWords[0] = Amor / userWords[1] = Roma
"""
userWords = data_request()
anagram(userWords[0], userWords[1])