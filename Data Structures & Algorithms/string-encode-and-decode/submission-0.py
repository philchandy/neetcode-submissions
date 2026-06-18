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
            separator_pos = s.find("#", pos)
            start = separator_pos + 1
            length = int(s[pos:separator_pos])
            end = start + length
            out.append(s[start:end])
            pos = end
        return out

