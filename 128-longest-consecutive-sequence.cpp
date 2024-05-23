class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() < 2) {
            return nums.size();
        }

        unordered_set<int> numSet;

        for (int i : nums) {
            numSet.insert(i);
        }

        int maxSeq = 1;

        for (int i : numSet) {
            if (numSet.count(i - 1) == 0) {
                int currNum = i, currSeq = 1;
                while (numSet.count(currNum + 1) != 0) {
                    currNum++;
                    currSeq++;
                }
                maxSeq = max(maxSeq, currSeq);
            }
        }
        return maxSeq;
    }
};
