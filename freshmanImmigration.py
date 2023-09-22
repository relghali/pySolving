# 1. reverse-string:
  class Solution(object):
    def reverseString(self, s):
        s= s.reverse()
        return s

# 2. two-sum:
class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (i+1, (len(nums))):
                if (nums[i]+nums[j]==target):
                    return [i, j]

# 3. length-of-last-word:
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        lastWord = ''
        for i in range (len(s)-1,-1,-1):
            if s[i]!=' ':
                lastWord+= s[i]
            else:
                return len(lastWord)
        if lastWord=='':
            return 0
        return len(lastWord)
