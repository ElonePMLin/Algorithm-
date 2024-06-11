class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        long long maxx = 0, summ = 0;
        for (int m : milestones) {
            maxx = max((long long) m, maxx);
            summ += (long long) m;
        }
        return maxx > summ - maxx + 1 ?  (summ - maxx) * 2 + 1 : summ;
    }
};


class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        long long maxx = ranges::max(milestones);
        long long summ = accumulate(milestones.begin(), milestones.end(), 0LL);
        return maxx > summ - maxx + 1 ?  (summ - maxx) * 2 + 1 : summ;
    }
};
