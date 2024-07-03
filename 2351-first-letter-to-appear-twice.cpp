class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_map<char, int> mp;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (mp.count(s[i]) == 0) {
                mp[s[i]] = i;
            } else {
                return s[i];
            }
        }

        return '\0';
    }
};
