class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def hammingWeight(n):
            count = 0 
            while n :
                n &= n-1
                count+=1
            return count 
        for i in range(n+1):
            res.append(hammingWeight(i))
        return res