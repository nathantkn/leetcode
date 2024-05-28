class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countMp;
        for (int num : nums) {
            countMp[num]++;
        }

        priority_queue<pair<int,int>> pq;
        for (auto i : countMp) {
            pq.push({i.second, i.first});
        }

        vector<int> res;
        while (k != 0 && !pq.empty()) {
            res.push_back(pq.top().second);
            pq.pop();
            k--;
        }

        return res;
    }
};
