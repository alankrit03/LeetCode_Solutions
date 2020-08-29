from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.isWord = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.pre = ''
        self.n = 0
        for word in words:
            curr = self.root
            word = word[::-1]
            for letter in word:
                curr = curr.dict[letter]
            curr.isWord = True

    def query(self, letter: str) -> bool:
        self.pre = letter+self.pre
        self.n+=1
        i=0
        curr = self.root
        while curr and i<self.n:
            curr = curr.dict[self.pre[i]]
            if curr.isWord:
                return True
            i+=1
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)