class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Keeps track of the non-zero elements
        count = 0
        
        # FOR : Traverse every element
        for i in nums:
            # If that particular index is a non zero element, we place the element in nums[count] & increment the value of count
            # EG : [0,1] -> For i=0, we check if condition, since it's 0, we aren't going to store the value. 
            # For i=1, we check nums[1] = 1, therefore we store nums[count] = nums[0] = 1 & count += 1
            if i != 0:
                nums[count] = i
                count += 1

        # After the above traversal is done, we move in the given range, & allot the remaining elements as 0
        for i in range(count, len(nums)):
            nums[i] = 0
