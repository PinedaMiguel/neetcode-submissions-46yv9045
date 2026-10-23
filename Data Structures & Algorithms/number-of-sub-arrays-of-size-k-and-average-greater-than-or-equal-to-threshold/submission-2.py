class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        ans = 0
        sumWindow = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                sumWindow -= arr[L]
                L += 1
            sumWindow += arr[R]
            if R - L + 1 == k and sumWindow / k >= threshold:
                ans += 1
        return ans
