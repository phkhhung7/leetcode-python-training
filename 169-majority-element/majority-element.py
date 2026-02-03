# Problem: Majority Element
# Pattern: Hash Table (Frequency Count)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Count frequency and return when count > n//2

class Solution:
    def majorityElement(self, nums):
        count = {}
        n = len(nums)

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 2:
                return num
