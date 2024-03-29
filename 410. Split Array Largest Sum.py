class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def Canit(target):
            sumi=0
            number_of_groups=1
            if (x<max(nums)):
                    return False  # for example if numsis[1,4,4] Canit(3) is False. we need this stattment epacially if we start 
                                  # from l=0; but if l=max(nums), we do nto need it.
            for n in nums:
                sumi+=n
                if sumi>target:
                    sumi=n
                    number_of_groups+=1
                    if number_of_groups>m:
                        return False
            
            return True
        
        l=max(nums)  
        r=0
        for n in nums:
            r+=n
        
        while l<=r:                     
            mid=(l+r)//2          
            
            if Canit(mid):
                ans=mid
                r=mid-1
                
            else:
                l=mid+1
        return ans
            
        
            
                    
