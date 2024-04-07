class Solution {
public:
    int numRabbits(vector<int>& answers) {
        int res = 0;
        map<int,int> rabbitCount;

        for (int curr : answers) {
            if (rabbitCount.find(curr) == rabbitCount.end() || rabbitCount[curr] == 0) {
                res += curr + 1;
                rabbitCount[curr] = curr;
            }
            else {
                rabbitCount[curr]--;
            }
        }
        return res;
    }
};
