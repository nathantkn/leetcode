class Solution {
public:
    int maxDepth(string s) {
        stack<char> charStack;
        int counter = 0;
        int maxCount = 0;

        for (char c : s) {
            if (c == '(') {
                counter++;
                charStack.push(c);
            }
            if (counter > maxCount) {
                maxCount = counter;
            }
            else if (c == ')' && charStack.top() == '(') {
                counter--;
            }
        }
        return maxCount;
    }
};
