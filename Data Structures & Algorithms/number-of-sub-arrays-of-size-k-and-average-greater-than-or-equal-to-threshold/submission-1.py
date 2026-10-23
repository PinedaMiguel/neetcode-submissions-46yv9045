class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = deque()
        L = 0
        ans = 0
        sumWindow = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                leftmost = window.popleft()
                sumWindow -= leftmost
                L += 1
            window.append(arr[R])
            sumWindow += arr[R]
            if len(window) == k and sumWindow / k >= threshold:
                ans += 1
        return ans
