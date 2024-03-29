# ref: https://www.youtube.com/watch?v=P6RZZMu_maU&ab_channel=NeetCode
# on youtube file the for loop is on nums, however it should be on numsSet to get it faster as there is no duplicat.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set(nums)        
        res=0
        # for n in nums: //if we loop on array rather than set
        # it will take more time due to duplicates.
        for n in numsSet:
            if n-1 in numsSet:
                continue       
            i=0    
            while (n+i) in numsSet:
                i+=1
            res=max(res,i)
        return res
                
