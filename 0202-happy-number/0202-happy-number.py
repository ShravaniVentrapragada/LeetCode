class Solution:
    def isHappy(self, n: int) -> bool:
      def get_n(n):
        total_sum = 0
        while n>0:
          n, digit = divmod(n, 10)
          total_sum += digit**2
        return total_sum
      seen = set()
      while n !=1 and n not in seen:
        seen.add(n)
        n = get_n(n)
        
      return n == 1
    