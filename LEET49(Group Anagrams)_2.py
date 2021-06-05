from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs):
        hash_map = {}

        for string in strs:
            count_map = {}

            for char in ascii_lowercase:
                count_map[char] = 0

            for char in string:
                count_map[char] += 1

            string_compare = ""
            for char, num in count_map.items():
                string_compare += (char + str(num))

            if string_compare not in hash_map:
                hash_map[string_compare] = [string]
            else:
                hash_map[string_compare].append(string)
        
        answer = hash_map.values()
        
        return answer

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))