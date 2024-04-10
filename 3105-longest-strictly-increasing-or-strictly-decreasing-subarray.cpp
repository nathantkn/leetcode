// MOST BALANCED
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        if (nums.size() == 1) {
            return 1;
        }

        int inc = 1, dec = 1, res = 1, currNum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > currNum) {
                inc++;
                res = max(res, inc);
            }
            else {
                inc = 1;
            }
            currNum = nums[i];
        }

        currNum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < currNum) {
                dec++;
                res = max(res, dec);
            }
            else {
                dec = 1;
            }
            currNum = nums[i];
        }
        return res;
    }
};

// 0 ms RUN TIME
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        if (nums.size() == 1) {
            return 1;
        }

        int inc = 1, dec = 1, res = 1, currNum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > currNum) {
                inc++;
            }
            else {
                inc = 1;
            }
            currNum = nums[i];
            res = max(res, inc);
        }

        currNum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < currNum) {
                dec++;
            }
            else {
                dec = 1;
            }
            currNum = nums[i];
            res = max(res, dec);
        }
        return res;
    }
};
