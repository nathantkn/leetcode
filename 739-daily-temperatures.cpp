class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        stack<int> stack;

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty()) {
                if (temperatures[stack.top()] > temperatures[i]) {
                    res[i] = stack.top() - i;
                    stack.push(i);
                    break;
                }
                stack.pop();
            }
            if (stack.empty()) {
                stack.push(i);
            }
        }

        return res;
    }
};
