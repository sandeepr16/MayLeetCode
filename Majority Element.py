$Python3
''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
''




class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        count=0
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key in d:
            if d[key] > len(nums) / 2: 
                count = 1
                return key 
