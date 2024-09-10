class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Q: To find 3 index in list (any index from left to right) which i < j < k

        # We set i,j to infinity
        i = j = float('inf')
        
        # FOR : Traverse every index & if index < i or index < j, we update them
        # And since we update i before j, i < j always
        for _ in range(nums)):
            if nums[_] <= i:
                i = nums[_}
            
            elif nums[_] <= j:
                j = nums[_]
        # When i,j updated, we return true if we found the third index (k) which therefore satisfy condition i < j < k
            else:
                return True

        return False
