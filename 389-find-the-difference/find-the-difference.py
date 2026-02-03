# Problem: Find the Difference
# Pattern: Bit Manipulation (XOR)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Key Idea: XOR các ký tự giống nhau sẽ triệt tiêu, còn lại là ký tự dư

class Solution:
    def findTheDifference(self, s, t):
        res = 0

        # XOR tất cả ký tự trong cả 2 chuỗi
        for c in s + t:
            res ^= ord(c)

        # Chuyển lại từ mã ASCII sang ký tự
        return chr(res)
