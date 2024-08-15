class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        print(s)
        pointer_one = 0
        pointer_two = len(s) - 1
        while(pointer_one < pointer_two):
            if not s[pointer_one].isalnum():
                pointer_one += 1
                continue
            if not s[pointer_two].isalnum():
                pointer_two -= 1
                continue
            if s[pointer_one].lower() != s[pointer_two].lower():
                return False
            pointer_one += 1
            pointer_two -= 1
        return True