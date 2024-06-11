// 获取最大值
//      .max_element(xx.begin(), xx.end());
//      ranges::min(xx);
class Solution {
public:
    int addedInteger(vector<int>& nums1, vector<int>& nums2) {
        return *max_element(nums2.begin(), nums2.end()) - *max_element(nums1.begin(), nums1.end());
    }
};


class Solution {
public:
    int addedInteger(vector<int>& nums1, vector<int>& nums2) {
        return ranges::min(nums2) - ranges::min(nums1);
    }
};
