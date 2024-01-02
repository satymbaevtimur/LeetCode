from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        nums.sort(reverse=True)
        
        matrix = []
        
        for num in nums:
            added = False
            for row in matrix:
                if num not in row:
                    row.append(num)
                    added = True
                    break
            
            if not added:
                matrix.append([num])
        
        return matrix
