import sys
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
            >>> s = Solution(); s.two_sum(nums=[2, 7, 11, 15], target=9)
            [0, 1]
            >>> s.two_sum(nums=[3, 2, 4], target=6)
            [1, 2]
            >>> s.two_sum(nums=[3, 3], target=6)
            [0, 1]
        """
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []


if __name__ == '__main__':
    import doctest
    doctest.testmod()

