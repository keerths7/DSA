'''
Problem: https://leetcode.com/problems/two-sum/description/
Find all pairs of integers whose sum is equal to a given number
'''
# Solution 1- Using Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_pairs_two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


# Solution 2- Using Brute Force with logic
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_pairs_two_sum_logic(nums,target):
    for i in nums:
        x = target - i
        if x in nums:
            return [nums.index(i), nums.index(x)]


# Solution 2- Using Brute Force with logic
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_pairs_two_sum_logic_enum(nums,target):
    for i, value in enumerate(nums):
        x = target - value
        if x in nums:
            return [i, nums.index(x)]
        
# Solution 2- Using Brute Force with logic
# Time Complexity: O(n^2)
# Space Complexity: O(1)
  
def find_pairs_two_sum_dict(nums,target):
    seen = {}
    for i, value in enumerate(nums):
        x = target - value
        if x in seen:
            return [seen[x], i]
        seen[value] = i
        

nums= [3,2,4,7]
target = 11
print(find_pairs_two_sum(nums, target))
print(find_pairs_two_sum_logic(nums,target))
print(find_pairs_two_sum_logic_enum(nums,target))
print(find_pairs_two_sum_dict(nums,target))