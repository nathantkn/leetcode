class Solution {
public:
    int currTimeToEat(vector<int>& piles, int mid, int h) {
        int totalHours = 0;

        for (int pile : piles) {
            int div = pile / mid;
            totalHours += div;
            if (pile % mid != 0) {
                totalHours++;
            }
        }
        return totalHours;
    }


    int minEatingSpeed(vector<int>& piles, int h) {
        int hi = 0, lo = 1;
        for (int i : piles) {
            if (i > hi) {
                hi = i;
            }
        }

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int currTime = currTimeToEat(piles, mid, h);
            if (currTime <= h) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
