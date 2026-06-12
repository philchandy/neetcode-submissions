class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_dict = {}
        for word in strs:
            sorted_letters = "".join(sorted(word))
            if sorted_letters not in letter_dict:
                letter_dict[sorted_letters] = [word]
            else:
                letter_dict[sorted_letters].append(word)
        
        return list(letter_dict.values())
    