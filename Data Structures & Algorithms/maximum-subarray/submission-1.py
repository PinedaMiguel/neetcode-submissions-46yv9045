class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            curr_sum = n + max(curr_sum, 0)
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum