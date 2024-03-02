# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, list):
        anagram = []
        for list_word in list:
            if sorted(self.word) == sorted(list_word.lower()):
                anagram.append(list_word)
        return anagram
    

    #The sorted() function is used to create sorted lists of characters
    #for both self.word and list_word.
    #If the sorted lists are equal, it means the words contain the same 
    #letters, even if those letters are arranged differently, indicating an anagram.