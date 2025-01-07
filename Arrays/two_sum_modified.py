'''
Problem: https://leetcode.com/problems/two-sum/description/
Find location of all distinct pairs of integers whose sum is equal to a given number
'''
# Solution 1- Using Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_pairs_two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                return [i,j]

        
# Solution 4- Using logic with dict
# Time Complexity: O(n)
# Space Complexity: O(1)
  
def find_pairs_two_sum_dict(nums,target):
    seen = {}
    for i, value in enumerate(nums):    # O(n)
        x = target - value
        if x in seen and x != value:    # O(1) for in operator used with dict
            return [seen[x], i]
        seen[value] = i
        

nums= [3,4,3,2]
target = 6
print(find_pairs_two_sum(nums, target))
print(find_pairs_two_sum_dict(nums,target))