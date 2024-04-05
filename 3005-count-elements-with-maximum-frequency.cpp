class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        map<int, int> countMap;
        int maxFreq = 0, elements = 0;

        for (int num : nums) {
            countMap[num]++;
            if (countMap[num] > maxFreq) {
                maxFreq = countMap[num];
                elements = countMap[num];
                continue;
            }
            if (countMap[num] == maxFreq) {
                elements += countMap[num];
            }
        }

        return elements;
    }
};
