class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        returned_value = 0
        char_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            returned_value = max(returned_value, r - l + 1)
        return returned_value