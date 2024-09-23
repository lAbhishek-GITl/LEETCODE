class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two Pointer Approach
        # Initialize left & right pointers
        left, right = 0, len(height) - 1
        result = 0
        
        # WHILE : Keeping right pointer ahead of left
        while left < right:
            # Calculate area, and compare with result each time
            area = (right - left) * min(height[right], height[left])
            result = max(result, area)

            # CONDITION : If height of left index < height of right index, we increment left index
            if height[left] < height[right]:
                left += 1
            # ELSE : Decrement right index
            else:
                right -= 1
        
        return result
            
        
