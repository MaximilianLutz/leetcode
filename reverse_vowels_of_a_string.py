class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s.strip(""))
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(word)-1

        # Start loop that ends when pointers meet in the  middel
        while start < end:
            while start < end and word[start] not in vowels:
                start += 1
            while start < end and word[end] not in vowels:
                end -= 1
            word[start], word[end] = word[end], word[start]

            start += 1
            end -= 1

        return(''.join(word))
