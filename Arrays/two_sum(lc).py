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


# Solution 2- Using logic with lists
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_pairs_two_sum_logic(nums,target):
    for i in nums:      # O(n)
        x = target - i
        if x in nums:    # O(n) for in operator used with lists                    
            return [nums.index(i), nums.index(x)]   # O(n) + O(n) = O(2n) to calculate index


# Solution 3 - Using logic with lists and enum
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_pairs_two_sum_logic_enum(nums,target):
    for i, value in enumerate(nums): # O(n)
        x = target - value
        if x in nums:       # O(n) for in operator used with lists
            return [i, nums.index(x)]   # O(n) to calculate index
        

# Solution 4- Using logic with dict
# Time Complexity: O(n)
# Space Complexity: O(1)
  
def find_pairs_two_sum_dict(nums,target):
    seen = {}
    for i, value in enumerate(nums):    # O(n)
        x = target - value
        if x in seen:    # O(1) for in operator used with dict
            return [seen[x], i]
        seen[value] = i
        

nums= [3,2,4,7]
target = 11
print(find_pairs_two_sum(nums, target))
print(find_pairs_two_sum_logic(nums,target))
print(find_pairs_two_sum_logic_enum(nums,target))
print(find_pairs_two_sum_dict(nums,target))