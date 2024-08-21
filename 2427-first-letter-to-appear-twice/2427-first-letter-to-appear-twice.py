class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_list = []
        for char in s:
            if char in letter_list:
                return char
            else: 
                letter_list.append(char)