class Solution:
    def reverseVowels(self, s: str) -> str:
        split_string = list(s.strip(""))
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


        ram_vowels = []
        ram_indexes = []

        for index, item in enumerate(split_string):
            if item in vowels:
                ram_vowels.insert(0, item)
                ram_indexes.append(index)

        for index, item in enumerate(ram_indexes):
            split_string[item] = ram_vowels[index]
        result = ''.join(split_string)
        return result