# Problem: Ransom Note
# Pattern: Hash Table (Counter)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Đếm tần suất ký tự trong magazine, sau đó trừ cho ransomNote
#           Nếu còn dư nghĩa là thiếu ký tự

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        # Đếm tần suất của từng ký tự
        r = Counter(ransomNote)
        m = Counter(magazine)

        # Nếu r - m còn phần tử → thiếu ký tự → False
        return not (r - m)
