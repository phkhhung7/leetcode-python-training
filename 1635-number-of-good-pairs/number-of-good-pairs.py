# Problem: Number of Good Pairs
# Pattern: Hash Table + Math
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Nếu một số xuất hiện v lần thì số cặp = v * (v - 1) / 2

from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        count = Counter(nums)

        # Tính tổng số cặp theo công thức tổ hợp
        return sum(v * (v - 1) // 2 for v in count.values())
