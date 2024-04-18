'''
TWO SUM LEETCODE CHALLENGE

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

# Brute Force Solution check every combination of two values and see if the sum equals the target. Start at the first indice and check each indice after that indice to see if it sums to target.  n * n -> O (n^2) When the outer loop i is looking at one index, the inner loop checks the value of i against all of the values of other indices in the list. 
class Solution:
    def brute_two_sum(self, nums: list[int], target: int) -> list[int]:
        # loops thru length of list
        for i in range(len(nums)):
            # inner loop starts at i+1 to avoid looping same element twice
            for j in range(i+1, len(nums)):
                # if value at index i + value at index j = target
                if (nums[i] + nums[j]) == target:
                    # return the index of those values
                    return [i, j]
        # return empty list if not pair found
        return []

random_list = [2, 3, 4, 5]
random_target = 9

brute_force_solution = Solution()
print(brute_force_solution.brute_two_sum(random_list, random_target))

# Soltion : [1, 2]


# create a hashmap to store [value, index] pairs. Use enumerate function to get get the index and the value at each index in the nums list. For each index calculate the difference between the target and the value of the num index. check if that difference is found in the list of nums return the key, which in this case is the value and its index.  if that value not found in the hashmap, add the key (num) and itss value (index) to the map. 

import enum


class Solution:
    def hashmap_two_sum(self, nums: list[int], target: int) -> list[int]:
        # create dictionary to store values (elements) and their indexes
        hashmap_storage = {}
        # iterate over the indices 'i' and values 'num' of each item in nums list
        for i, num in enumerate(nums):
            difference = target - num 
        # check if calculate value in dictionary
            if difference in hashmap_storage and hashmap_storage[difference] != i:
        # if difference found, return the indices of the of the two values (elements) that add up to the target
                return [hashmap_storage[difference], i]  
        # if difference value not found, add the current value and its index to the dictionary
            hashmap_storage[num] = i 
    
random_list = [2, 6, 9, 3]
random_target = 5

hashmap_solution = Solution()
print(hashmap_solution.hashmap_two_sum(random_list, random_target))