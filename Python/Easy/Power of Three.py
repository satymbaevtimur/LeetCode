class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return math.ceil(math.log10(n) / math.log10(3)) == math.floor(math.log10(n) / math.log10(3)) if n > 0 else False
