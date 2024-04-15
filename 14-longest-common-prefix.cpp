class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int shortestIndex = 0;

        for (int i = 0; i < strs.size(); i++) {
            if (strs[i].length() < strs[shortestIndex].length()) {
                shortestIndex = i;
            }
        }

        string prefix = strs[shortestIndex];
        for (int i = 0; i < strs.size(); i++) {
            if (i == shortestIndex) {
                continue;
            }

            for (int j = 0; j < prefix.length(); j++) {
                if ((strs[i])[j] != prefix[j] && j != 0) {
                    prefix = prefix.substr(0, j);
                } else if ((strs[i])[j] != prefix[j] && j == 0) {
                    prefix = "";
                }
            }
        }
        return prefix;
    }
};
