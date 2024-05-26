class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (string str : strs) {
            res += str.length();
            res += "#" + str;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;

        while (i < s.length()) {
            int j = i + 1;
            if (s[j] != '#') {
                j++;
            }
            string newStr = s.substr(j + 1, s[i]);
            res.push_back(newStr);
            i = s[i] + j + 1;
        }

        return res;
    }
};
