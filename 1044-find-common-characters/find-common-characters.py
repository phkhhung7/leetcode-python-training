# Problem: Find Common Characters
# Pattern: Hash Table Intersection
# Time Complexity: O(n * k)
# Space Complexity: O(n)
# Key Idea: Giao Counter để lấy tần suất nhỏ nhất của mỗi ký tự

from collections import Counter

class Solution:
    def commonChars(self, words):
        # Khởi tạo bằng từ đầu tiên
        common = Counter(words[0])

        # Lấy giao với các từ còn lại
        for w in words[1:]:
            common &= Counter(w)

        # Bung kết quả thành list ký tự
        return list(common.elements())
