class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) {
            return 0;
        }

        int profit = 0;
        int minPrice = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else {
                profit = max(profit, prices[i] - minPrice);
            }
        }
        return profit;
    }
};
