class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        answer = 0
        current = 0
        
        for right in range(len(nums)):
            target = nums[right]
            current += target
            
            while (right - left + 1) * target - current > k:
                current -= nums[left]
                left += 1
            
            answer = max(answer, right - left + 1)

        return answer
