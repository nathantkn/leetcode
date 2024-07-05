class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> res;
        string prevWord;

        for (string word : words) {
            string currWord = word;
            sort(currWord.begin(), currWord.end());

            if (prevWord != currWord) {
                res.push_back(word);
                prevWord = currWord;
            }
            
        }

        return res;
    }
};
