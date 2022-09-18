class Solution:
    def findNumbers(self, nums: List[int]) -> int:
      even = 0
      for i in nums:
        length = len(str(i))
        if length % 2 == 0:
          even +=1
      return even