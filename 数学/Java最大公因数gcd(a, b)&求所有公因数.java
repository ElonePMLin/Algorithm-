class Solution {
    public int commonFactors(int a, int b) {
        int g = gcd(a, b), ans = 0;
        for (int i = 1; i * i <= g; i++) {
            if (g % i == 0) {
                ++ans;
                if (i * i < g) {
                    ++ans;
                }
            }
        }
        return ans;
    }

    public int gcd(int a, int b) {
        while (a != 0) {
            int tmp = a;
            a = b % a;
            b = tmp;
        }
        return b;
    }
}