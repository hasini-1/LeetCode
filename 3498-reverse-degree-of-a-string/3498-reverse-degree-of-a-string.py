class Solution(object):
    def reverseDegree(self, s):
        result = 0
        for i in range(len(s)):
            position = i+1
            value = ord('z') - ord(s[i]) + 1
            result += value * position
        return result
        """
        :type s: str
        :rtype: int
        """
        