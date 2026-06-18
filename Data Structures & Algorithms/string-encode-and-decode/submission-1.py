class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word)) + "#" + word
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        pos = 0
        while pos < len(s):
            sep = s.find("#", pos)
            length = int(s[pos:sep])

            out.append(s[sep + 1 : sep + length + 1])
            pos = sep + length + 1
        return out

