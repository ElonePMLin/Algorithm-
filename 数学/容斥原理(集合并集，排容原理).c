// 求从 1 ～ n，能被 3，5，7 整除的总数


class Solution {
public:
    int sumOfMultiples(int n) {
        return summ(3, n) + summ(5, n) + summ(7, n) - summ(15, n) - summ(21, n) - summ(35, n) + summ(105, n);
    }

    int summ(int m, int n) {
        return n / m * (n / m + 1) / 2 * m;  // 等差数列
    }
};