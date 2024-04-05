class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> countMap;
        vector<int> res;

        for (int num: nums1) {
            if (countMap[num] == 0) {
                countMap[num]++;
            }
        }

        for (int num : nums2) {
            if (countMap[num] > 0 && countMap[num] < 2) {
                res.push_back(num);
                countMap[num]++;
            }
        }

        return res;
    }
};
