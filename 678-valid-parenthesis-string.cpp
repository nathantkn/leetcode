class Solution {
public:
    bool checkValidString(string s) {
        stack<int> bracketStack;
        stack<int> asteriskStack;

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (c == '(') {
                bracketStack.push(i);
            }
            else if (c == '*') {
                asteriskStack.push(i);
            }
            else {
                if (!bracketStack.empty()) {
                    bracketStack.pop();
                }
                else if (!asteriskStack.empty()) {
                    asteriskStack.pop();
                }
                else {
                    return false;
                }
            }
        }
        
        while (!bracketStack.empty() && !asteriskStack.empty()) {
            if (bracketStack.top() > asteriskStack.top()) {
                return false;
            }
            asteriskStack.pop();
            bracketStack.pop();
        }
        return bracketStack.empty();
    }
};
