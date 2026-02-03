# Problem: Valid Anagram
# Pattern: Hash Table (Frequency Count)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Count characters in s, then decrement using t

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Decrement using t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True
