from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Create a dictionary to store elements and their indices
        
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach the target
            if complement in num_indices:
                return [num_indices[complement], i]  # If the complement is in the dictionary, return the indices
            num_indices[num] = i  # Otherwise, add the current number and its index to the dictionary


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]