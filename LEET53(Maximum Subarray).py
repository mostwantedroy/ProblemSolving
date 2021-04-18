class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)

        dp = [ None for _ in range(length) ]
        start_idx = [ 0 for _ in range(length) ]

        dp[0] = nums[0]

        for i in range(1, length):
            if nums[i] + dp[i - 1] > nums[i]:
                dp[i] = dp[i - 1] + nums[i]
                start_idx[i] = start_idx[i - 1]
            else:
                dp[i] = nums[i]
                start_idx[i] = i

        return max(dp)