class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for i in words:
            common &= Counter(i) 
        return list(common.elements())
