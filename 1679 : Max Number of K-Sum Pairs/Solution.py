class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Q: We have to count number pair which sum up to k, conditioned, no index is repeated in the count pair
        # Two Pointer Approach
        # Sort the array to eliminate any back tracking n

        nums = sorted(nums)

        left, right = 0, len(nums) - 1
        count = 0

        # WHILE : Left < Right
        while left < right:
            # Check for current sum
            current_sum = nums[left] + nums[right]

            # Condition: If current sum achived, we increase count and move to next index from both side
            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            # CONDITION : If current sum lesser than required, then we move from left because left side is lesser
            elif current_sum < k:
                left += 1
            
            # CONDITION : If current sum bigger than target, we move from right side because bigger numbers are on right side
            else:
                right -= 1

        return count

            


        
