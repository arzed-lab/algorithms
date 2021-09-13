# 209. Minimum Size Subarray Sum | Leetcode.com

# Given an array of positive integers nums and a positive integer target, return the minimal 
# length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
#  of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = 999
        curr_size = 0
        i = 0
        count = 0
        while i < len(nums):
            curr_size += nums[i]
            count += 1
            if curr_size >= target:
                curr_size = 0
                if min_size > count:
                    min_size = count    
                    count = 0
            i += 1
        if min_size != 999:
            return min_size 
        else:
            return 0


res = Solution()
nums = [1,2,3,4,5]
target = 11

print(res.minSubArrayLen(target,nums))

