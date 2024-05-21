class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int lowest = INT_MAX, secondLowest = INT_MAX;

        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < lowest) {
                secondLowest = lowest;
                lowest = prices[i];
            } 
            else if (prices[i] < secondLowest) {
                secondLowest = prices[i];
            }
        }

        int res = money - (lowest + secondLowest);

        if (res >= 0) {
            return res;
        } else {
            return money;
        }
    }
};
