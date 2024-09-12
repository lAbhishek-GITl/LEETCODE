class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Q: We have to find strings that are made up of characters in allowed only

        # Lenght of list
        n = len(words)
        
        # FOR : Traverse the index in words
        for i in words:
            # Travers the characters in particular indexes
            for j in i:
                # If the string contains any other characters, we decrease the length of the array which will finally be returned
                if j not in allowed:
                    n -= 1
                    break

        return n
        
