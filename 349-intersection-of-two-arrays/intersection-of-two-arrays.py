# Problem: Intersection of Two Arrays
# Pattern: Hash Set
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Key Idea: Convert arrays to sets and take their intersection

class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
