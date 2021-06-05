class Solution:
    def groupAnagrams(self, strs):
        hash_map = {}
        
        for string in strs:
            string_compare = "".join(sorted(string))
            
            if string_compare not in hash_map:
                hash_map[string_compare] = [string]
            else:
                hash_map[string_compare].append(string)
        
        answer = hash_map.values()
        
        return answer