class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = deque()
        L = 0
        ans = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                window.popleft()
                L += 1
            window.append(arr[R])
            if len(window) == k and sum(window) / len(window) >= threshold:
                ans += 1
        return ans
