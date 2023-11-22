class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return math.ceil(math.log10(n) / math.log10(4)) == math.floor(math.log10(n) / math.log10(4)) if n > 0 else False
