# 1351. Count Negative Numbers in a Sorted Matrix | Leetcode.com

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
# return the number of negative numbers in grid.

from typing import List

class Solution:
    def __init__(self) -> None:
        pass
    def countNegatives(self, grid: List[List[int]]) -> int:
        times = 0
        for element in grid:
            low = 0
            high = len(element) 
            while 0 < high:
                high = high - 1
                if 0  < element[high]:
                    break
                elif 0  > element[high]:
                    times += 1
        return times

result = Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])

print(result)
