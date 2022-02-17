from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Solution when complexity = O(n)
        # for index, item in enumerate(nums):
        #     if item == target:
        #         return index
        #     if index == len(nums) - 1:
        #         return -1

        # Solution when complexity = O(log n)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
            if target == nums[mid]:
                return mid
        return -1


f = Solution()
test_array = [-1,0,3,5,9,12]
target = 6

print(f.search(test_array, target))