class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        result = 0
        for value in dictionary.values():
            if value == 1:
                return -1
            else:
                if value % 3 == 0:
                    result += value // 3 
                else:
                    result += value // 3 + 1
        
        return result
