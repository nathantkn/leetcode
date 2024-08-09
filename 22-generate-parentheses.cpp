class Solution {
public:
    void _generate(vector<string>& res, string curr, int open, int close) {
        if (open == 0 && close == 0) {
            res.push_back(curr);
            return;
        }

        if (open == close) {
            _generate(res, curr + "(", open - 1, close);
        }
        else if (open == 0) {
            _generate(res, curr + ")", open, close - 1);
        }
        else {
            _generate(res, curr + "(", open - 1, close);
            _generate(res, curr + ")", open, close - 1);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        _generate(res, "", n, n);
        return res;
    }
};
