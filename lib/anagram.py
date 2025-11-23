class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        return [word for word in possible_anagrams if sorted(word.lower()) == sorted(self.word.lower())]
