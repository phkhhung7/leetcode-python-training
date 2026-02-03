# Problem: Relative Sort Array
# Pattern: Hash Map + Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Key Idea: Count frequency and rebuild array based on arr2

class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import Counter

        count = Counter(arr1)
        result = []

        # Add elements in the order of arr2
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        # Add remaining elements sorted
        for num in sorted(count.keys()):
            result.extend([num] * count[num])

        return result
