from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        count = 0

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i].get(diff, 0) + 1

                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    count += dp[j][diff]

        return count
