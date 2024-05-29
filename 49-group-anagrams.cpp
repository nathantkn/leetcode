class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> charMap;
        int n = strs.size();

        for (string str : strs) {
            string tempStr = str;
            sort(tempStr.begin(), tempStr.end());
            charMap[tempStr].push_back(str);
        }

        vector<vector<string>> res;
        for (auto i : charMap) {
            res.push_back(i.second);
        }
        return res;
    }
};
