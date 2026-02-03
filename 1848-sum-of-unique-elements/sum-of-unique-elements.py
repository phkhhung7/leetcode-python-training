# Problem: Sum of Unique Elements
# Pattern: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Chỉ cộng những số có tần suất = 1

from collections import Counter

class Solution:
    def sumOfUnique(self, nums):
        count = Counter(nums)

        # Cộng các số xuất hiện đúng 1 lần
        return sum(x for x, v in count.items() if v == 1)
