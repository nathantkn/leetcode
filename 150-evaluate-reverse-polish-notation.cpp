class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numStack;

        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                numStack.push(stoi(tokens[i]));
            }
            else {
                int secondNum = numStack.top();
                numStack.pop();
                int firstNum = numStack.top();
                numStack.pop();
                if (tokens[i] == "+") {
                    numStack.push(firstNum + secondNum);
                }
                else if (tokens[i] == "-") {
                    numStack.push(firstNum - secondNum);
                }
                else if (tokens[i] == "*") {
                    numStack.push(firstNum * secondNum);
                }
                else if (tokens[i] == "/") {
                    numStack.push(firstNum / secondNum);
                }
            }
        }

        return numStack.top(); 
    }
};
