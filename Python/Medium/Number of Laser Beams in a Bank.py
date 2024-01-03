class Solution:
    def numberOfBeams(self, bank):
        answer, temporary = 0, 0
        
        for string in bank:
            count = string.count('1')
            
            if count == 0:
                continue
            
            answer += temporary * count
            temporary = count
        
        return answer
