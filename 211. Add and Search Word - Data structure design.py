class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for letter in word:

            if not curr.get(letter):
                curr[letter] = dict()

            curr = curr[letter]
        curr['word'] = True

    def search(self, word) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)

        def recur(node, i):
            if type(node) is bool:
                return False

            if i == n:
                return node.get('word', False)

            if word[i] in node:
                return recur(node[word[i]], i + 1)
            ans = False
            if word[i] == '.':
                for key in node.keys():
                    ans = ans or recur(node[key], i + 1)
                    if ans:
                        return ans
            return ans

        return recur(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)