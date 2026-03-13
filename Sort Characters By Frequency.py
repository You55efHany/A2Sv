from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        a = sorted(list(s),key=lambda x:(cnt[x],x),reverse=True)
        return ''.join(a)
