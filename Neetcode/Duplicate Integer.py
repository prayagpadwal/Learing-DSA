# EASY
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

# Approach 1 - sort then compare each element with previous
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        nums.sort()

        for i in range(len(nums)-1):
            j = i + 1

            if nums[i] != nums[j]:
                j += 1
            else:
                return True
        return False

# Approach 2 - using set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        return len(set(nums)) != len(list(nums))