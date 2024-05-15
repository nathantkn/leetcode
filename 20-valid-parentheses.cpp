class Solution {
public:
    bool isValid(string s) {
        stack<char> charStack;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                charStack.push(s[i]);
                continue;
            }
            else if (s[i] == ')' && !charStack.empty() && charStack.top() == '(') {
                charStack.pop();
                continue;
            }
            else if (s[i] == '}' && !charStack.empty() && charStack.top() == '{') {
                charStack.pop();
                continue;
            }
            else if (s[i] == ']'&& !charStack.empty() && charStack.top() == '[') {
                charStack.pop();
                continue;
            }
            return false;
        }
        if (!charStack.empty()) {
            return false;
        }
        return true;
    }
};
