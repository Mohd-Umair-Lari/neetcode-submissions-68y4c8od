class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      n = len(nums)
      i = 0
      while(i < n):
        if nums[abs(nums[i]) - 1] < 0:
            return abs(nums[i])
        nums[abs(nums[i]) - 1] *= -1
        i += 1
         


        
        
    
            
