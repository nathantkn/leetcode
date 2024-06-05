class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = set(words[0])
        res = []

        for ch in chars: 
            freq = min([word.count(ch) for word in words])
            res += ch * freq
        return res

    def commonChars2(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        allFreqCount = Counter(words[0])

        for i in range(1, n):
            currFreqCount = Counter(words[i])

            for key in allFreqCount.keys():
                allFreqCount[key] = min(allFreqCount[key], currFreqCount[key])

        for key, value in allFreqCount.items():
            for i in range(value):
                res.append(key)

        return res
