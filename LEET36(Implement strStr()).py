class Solution:
    def __init__(self):
        self.hash_map = {}

    def strStr(self, haystack: str, needle: str) -> int:
        length_haystack = len(haystack)
        length_needle = len(needle)

        if length_needle == 0:
            return 0

        if length_haystack == 1 and length_haystack == length_needle:
            return 0 if haystack == needle else -1

        for i in range(0, length_haystack - length_needle + 1):
            key = haystack[i:i + length_needle]
            if not key in self.hash_map:
                self.hash_map[key] = i

        if needle in self.hash_map:
            return self.hash_map[needle]

        return -1