class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_numbers = set([i for i in range(len(nums)+1)])
        for i in nums:
            all_numbers.remove(i)
        return all_numbers.pop()