# Problem: Maximum Number of Balloons
# Pattern: Hash / Frequency Counting
# Time Complexity: O(n)
# Space Complexity: O(1) (fixed alphabet size)
# Key Idea: Count characters and find the minimum ratio

class Solution:
    def maxNumberOfBalloons(self, text):
        from collections import Counter

        count = Counter(text)

        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )
