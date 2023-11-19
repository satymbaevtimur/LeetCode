class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0

        nums.sort()
        steps = 0
        stepUp = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                stepUp += 1

            steps += stepUp

        return steps
