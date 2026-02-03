# Problem: Jewels and Stones
# Pattern: Set Lookup
# Time Complexity: O(n)
# Space Complexity: O(k)
# Key Idea: Chuyển jewels thành set để kiểm tra nhanh O(1)

class Solution:
    def numJewelsInStones(self, jewels, stones):
        # Set giúp tra cứu nhanh hơn list
        jewel_set = set(jewels)

        # Đếm số ký tự trong stones xuất hiện trong jewel_set
        return sum(1 for s in stones if s in jewel_set)
