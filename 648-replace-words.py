class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
            

    def searchPrefix(self, word: str) -> str:
        curr = self.root
        res = ""

        for c in word:
            if c not in curr.children:
                return ""

            curr = curr.children[c]
            res = res + c

            if curr.end == True:
                break
            
        return res

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        words = sentence.split()
        res = []

        for word in dictionary:
            trie.insert(word)

        for i in range(len(words)):
            newWord = trie.searchPrefix(words[i])
            if newWord != "":
                words[i] = newWord
        
        return ' '.join(words)
