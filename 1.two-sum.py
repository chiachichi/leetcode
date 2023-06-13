#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

# class Solution:
#     ''' Brute Force Solution
    
#     Time Complexity: O(n^2)
#     Space Complexity:O(1)
#     '''
#     # legacy
#     # def twoSum(self, nums: List[int], target: int) -> List[int]:
#     #     for id1, num1 in enumerate(nums):
#     #         for id2, num2 in enumerate(nums[id1+1:]):
#     #             if num1 + num2 == target:
#     #                 return [id1, id1+1+id2]
#     # don't have to specify variables to numbers
    
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
                
class Solution:
    ''' One-pass Hash Map Solution

    1. check if current element's complement already exists in the hash table. 
    2. If it exists, we have found a solution and return the indices immediately.
    3. If not, we insert the element and index to the hash table.

    - Time Complexity: O(n)
    
    for loop: n times execution
    statement inside loop: constant times execution
    -> n + k*n = (k+1)*n times execution
    -> O(n)
    
    - Space Complexity: O(n)

    hashmap: at most (n-1) elements
    others: O(1) which can be ignored
    -> O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

# if __name__ == "__main__":
#     nums = [2,7,11,15]
#     target = 9
#     output = [0,1]
#     result = Solution().twoSum(nums, target)
#     if result == output:
#         print(f"The solution is correct!")
#     else:
#         print(f"The solution is wrong: right anser is {output} but yours is {result}.")
        
#     nums = [3,2,4]
#     target = 6
#     output = [1,2]
#     result = Solution().twoSum(nums, target)
#     if result == output:
#         print(f"The solution is correct!")
#     else:
#         print(f"The solution is wrong: right anser is {output} but yours is {result}.")
        
#     nums = [3,3]
#     target = 6
#     output = [0,1]
#     result = Solution().twoSum(nums, target)
#     if result == output:
#         print(f"The solution is correct!")
#     else:
#         print(f"The solution is wrong: right anser is {output} but yours is {result}.")
        
# @lc code=end

