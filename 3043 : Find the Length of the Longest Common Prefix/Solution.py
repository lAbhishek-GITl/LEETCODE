class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # Ensure array1 always smaller than array2
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        #Initialize a set to store prefixes
        prefix = set()

        # FOR : We go through every element in array1
        for i in arr1:
            # WHILE : i is non zero & not present in prefix set, we add it to prefix set & divide the number by 10
            while i and i not in prefix:
                prefix.add(i)
                i = i // 10
        
        result = 0

        # FOR: We go through array 2 and repeat the while loop for the same
        for j in arr2:
            while j and j not in prefix:
                j = j // 10

            # CONDITION : If j is non zero, we compare it with result & its length, we return max
            if j:
                result = max(result, len(str(j)))

        return result

        
