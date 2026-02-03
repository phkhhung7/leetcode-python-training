# Problem: Two Sum
# Pattern: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Lưu số đã gặp để kiểm tra bù

class Solution:
    def twoSum(self, nums, target):
        mp = {}  # value -> index

        for i, n in enumerate(nums):
            need = target - n
            if need in mp:
                return [mp[need], i]
            mp[n] = i
