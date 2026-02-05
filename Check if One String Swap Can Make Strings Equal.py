class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        return len(diffs) == 0 or (len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]])
