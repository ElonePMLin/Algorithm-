class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int ans = 0, n = arr.length;
        for (int i = 0; i < n; i++) {
            int left = i, right = n - 1 - i;
            int leftOdd = (left + 1) / 2, rightOdd = (right + 1) / 2;
            int leftEven = left / 2 + 1, rightEven = right / 2 + 1;
            ans += arr[i] * (leftOdd * rightOdd + leftEven * rightEven);
        }
        return ans;
    }
}