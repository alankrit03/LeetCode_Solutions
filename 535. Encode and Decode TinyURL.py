class Codec:

    def __init__(self):
        self.dic = {}
        self.n = 1
        self.cons = 'http://tiny.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.dic[self.n] = longUrl

        url = str(self.n)
        self.n += 1
        return self.cons + url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = ''
        for x in shortUrl[::-1]:
            if x == '/':
                break
            s = x + s

        return self.dic[int(s)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))