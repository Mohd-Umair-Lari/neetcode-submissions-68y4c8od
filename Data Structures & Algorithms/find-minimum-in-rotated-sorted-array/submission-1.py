class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        

        while(l < r):
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1

            elif nums[r] >= nums[m]:
                r = m

        return nums[l]
            