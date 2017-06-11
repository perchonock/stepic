class PatternSearcher:
    def __init__(self, pattern, text):
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pattern_len = len(pattern)
        self.hashes = [None for i in range(self.text_len - self.pattern_len + 1)]
        self.pattern_hash = self.hash(self.pattern)

    def hash(self, str):
        l = len(str)
        self.x = 263
        self.p = 1000000007
        sum = 0
        mult = 1
        for i in range(l):
            sum += ord(str[i]) * mult
            sum %= self.p
            self.mult_max = mult
            mult = (mult * self.x) % self.p
        return sum

    def recalc_hash(self, i):
        h_i = (self.hashes[i+1] - ord(self.text[i + self.pattern_len])*self.mult_max)*self.x + ord(self.text[i])
        h_i %= self.p
        return h_i

    def hash4text(self):
        last_index = self.text_len - self.pattern_len
        self.hashes[-1] = self.hash(self.text[last_index:])
        for i in range(last_index - 1, -1, -1):
            self.hashes[i] = self.recalc_hash(i)

    def search(self):
        result = ''
        self.hash4text()
        for i in range(len(self.hashes)):
            if self.hashes[i] == self.pattern_hash and self.pattern == self.text[i:i+self.pattern_len]:
                result += str(i) + ' '
        return result.strip()

pattern = input()
text = input()

h = PatternSearcher(pattern, text)
print(h.search())










