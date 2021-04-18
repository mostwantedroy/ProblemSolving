class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        output = []

        length = len(nums)
        for i in range(length - 2):
            target = nums[i]

            start = i + 1
            last = length - 1

            while start < last:
                if target + nums[start] + nums[last] > 0:
                    last -= 1
                elif target + nums[start] + nums[last] < 0:
                    start += 1
                else:
                    output.append([target, nums[start], nums[last]])
                    start += 1
                    last -= 1
                    
                    while nums[start - 1] == nums[start] and start < last:
                        start += 1
                    
                    while nums[last] == nums[last + 1] and start < last:
                        last -= 1
                
        return output
                
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
# -4 -1 -1 0 1 2