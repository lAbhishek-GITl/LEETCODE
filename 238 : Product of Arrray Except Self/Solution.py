class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Q: To print the product of every element in the list except itself

        # APPROACH: We take left & right product.
        # Left_Product : To multiply every element on the left side of that index
        # Right_Product : To multiply every element on the right side of that index

        # Count length, also initialize a result list of length n with every element being 1
        n = len(nums)
        result = [1] * n
        
        # It will store cumilative product of all elements on left side of index
        left_product = 1
        # FOR : Calculate left side product of every element
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # It will store cumilative product of all elements on right side of index
        right_product = 1
        # FOR : Calculate right side product of every elements
        for j in range(n - 1, -1, -1):
            result[j] *= right_product
            right_product *= nums[j]

        
        return result
        
