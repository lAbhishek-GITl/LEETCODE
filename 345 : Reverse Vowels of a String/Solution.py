class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two Pointers Problem
        # Q: To reverse only the vowels in the given string

        # Define vowels, and make a list of the given string
        vowels = 'AEIOUaeiou'
        s_list = list(s)
        left, right = 0, len(s) - 1

        # WHILE : Left pointer < Right pointer
        while left < right:
            # Check for vowel character, if not found move to next index from left
            while left < right and s_list[left] not in vowels:
                left += 1
            # Check for vowel character, if not found move to next index from right
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # After checking done, when vowels found on both pointer, we swap
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        # Convert list to string again and return
        return ''.join(s_list)
