class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int x = 0; x <= n; x++) {
            int lo = 0, hi = n - 1, pos = n;

            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (nums[mid] >= x) {
                    pos = mid;
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            }

            if (n - pos == x) {
                return x;
            }
        }

        return -1;
    }
};
