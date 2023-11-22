class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return math.ceil(math.log10(n) / math.log10(2)) == math.floor(math.log10(n) / math.log10(2)) if n > 0 else False
