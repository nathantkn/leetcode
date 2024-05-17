class Solution {
public:
    bool isPalindrome(string s) {
        string newStr = "";
        for (char i : s) {
            if (isalnum(i)) {
                newStr += tolower(i);
            }
        }

        int j = newStr.length() - 1;
        for (int i = 0; i < j; i++) {
            if (newStr[i] != newStr[j]) {
                return false;
            }
        j--;
    }

        return true;
    }
};
