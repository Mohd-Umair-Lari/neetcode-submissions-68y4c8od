class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
    
        while(l < r):
            p = (l + r) // 2
            if nums[p] > nums[r]:
                l = p + 1
            else:
                r = p

        pivot = l             #found the pivot. (min element). left half -> l to m and right half is m to r
        
        def bs(l: int, r: int) -> int:
            while(l <= r):
                m = (l + r) // 2

                if target == nums[m]:
                    return m

                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        result = bs(0, pivot - 1)

        if result != -1:
            return result

        return bs(pivot, len(nums) - 1)
