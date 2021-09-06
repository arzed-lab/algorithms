# 167. Two Sum II - Input array is sorted | Leetcode.com

# Given an array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
# where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        sum = 0
        while start <= end :
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start +=1
            else:
                return [start+1,end+1]