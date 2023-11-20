class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total, travelTime = 0, 0
        total += len(garbage[0])
        lastGarbageIndexes = [-1, -1, -1]

        for i in range(1, len(garbage)):
            total += len(garbage[i])

            if "M" in garbage[i]:
                lastGarbageIndexes[0] = i - 1
            if "P" in garbage[i]:
                lastGarbageIndexes[1] = i - 1
            if "G" in garbage[i]:
                lastGarbageIndexes[2] = i - 1
            
        for i in range(len(travel)):
            travelTime += travel[i]

            for j in range(3):
                if lastGarbageIndexes[j] == i:
                    total += travelTime

        return total 
