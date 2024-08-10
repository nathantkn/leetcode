class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, double>> timeToTarget;
        

        for (int i = 0; i < n; i++) {
            timeToTarget.push_back(make_pair(position[i], (double)(target - position[i]) / (double)speed[i]));
        }

        sort(timeToTarget.begin(), timeToTarget.end());
        int fleet = 1, currTrackedFleet = n - 1; 
        for (int i = n - 2; i >= 0; i--) {
            if (timeToTarget[i].second > timeToTarget[currTrackedFleet].second) {
                currTrackedFleet = i;
                fleet++;
            }
        }

        return fleet;
    }
};
