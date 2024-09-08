class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Q: To reverse words (not characters) in given string

        # Split string in words in a list, without trailing or leading spaces
        words = s.split()
        
        # Reverse the list
        words.reverse()

        # Return list with a space, so words are separated
        return ' '.join(words)
