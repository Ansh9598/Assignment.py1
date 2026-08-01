class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] >= nums[mid]:
                if nums[left] >= target > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] > target >= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


obj = Solution()

print(obj.search([2, 1, 0, 7, 6, 5, 4], 6))   
print(obj.search([2, 1, 0, 7, 6, 5, 4], 3))   
print(obj.search([5, 4, 3, 2, 1], 4))         
print(obj.search([], 5))                      