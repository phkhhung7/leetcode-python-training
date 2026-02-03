# Problem: Intersection of Two Arrays II
# Pattern: Hash Table (Frequency Count)
# Time Complexity: O(n + m)
# Space Complexity: O(n)
# Key Idea: Count nums1, then decrement using nums2

class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        result = []

        # Count elements in nums1
        for n in nums1:
            count[n] = count.get(n, 0) + 1

        # Build intersection using nums2
        for n in nums2:
            if n in count and count[n] > 0:
                result.append(n)
                count[n] -= 1

        return result
