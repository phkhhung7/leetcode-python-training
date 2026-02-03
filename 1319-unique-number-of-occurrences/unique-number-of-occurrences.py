# Problem: Unique Number of Occurrences
# Pattern: Hash Table + Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Tần suất xuất hiện không được trùng nhau

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr).values()

        # Nếu tất cả tần suất là duy nhất thì set và list có cùng độ dài
        return len(set(freq)) == len(freq)
