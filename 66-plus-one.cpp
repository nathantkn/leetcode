class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool remainder = true;
        int i = digits.size() - 1;
        while (remainder) {
            remainder = false;
            if (i == -1) {
                digits.insert(digits.begin(), 1);
                break;
            }
            if (digits[i] != 9) {
                digits[i]++;
            }
            else {
                digits[i] = 0;
                remainder = true;
                i--;
            }
        }
        return digits;
    }
};
