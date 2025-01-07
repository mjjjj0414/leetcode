# Product of Array Except Self
from typing import List

class Solution: 
    def productExeptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

    # Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and combine with prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
       