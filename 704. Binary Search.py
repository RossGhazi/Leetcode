class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while True:
            if l>r:
                return -1                    
            m = (l + r) // 2            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1                 
            else:
                r = m - 1
