class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
      # BRUTE FORCE METHOD
      # Go through every element present in the array using two pointer approach

        # Stores the area of every 2 elements 
        result = 0

        # FOR : Left pointer
        for i in range(len(height) - 1):
          # FOR : Right pointer which will always stay ahead of left pointer
            for j in range(i + 1, len(height)):
              # Area
                a = (j - i) * (min(height[i], height[j]))
              # Store maximum result
                result = max(result, a)

        return result
        
