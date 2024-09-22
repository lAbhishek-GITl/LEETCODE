class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Two pointer approach
        first, last = 0, 0

        # WHILE : We traverse through both strings 
        # First : will go through sub string, Last : Will go through major string
        while first < len(s) and last < len(t):
            # CONDITION : If we find both characters to be matching, we increment first
            if s[first] == t[last]:
                first += 1
            # We increment last no matter if we find match or not
            last += 1

        # We return true if first has traversed through all the elements
        return first == len(s)
