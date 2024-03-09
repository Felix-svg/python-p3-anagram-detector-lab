class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagrams = []
        for i in list:
            if sorted(self.word) == sorted(i):
                anagrams.append(i)
        return anagrams
