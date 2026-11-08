class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        total = int(0.5*(n*(n+1)))
        for num in nums:
            total-=num
        return total