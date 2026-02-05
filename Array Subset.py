from collections import Counter

class Solution:
    def isSubset(self, a, b):
        c = Counter(a);
        for i in b:
            if i not in c or c[i] <= 0:
                return False
            c[i] -= 1
        return True

                
    
    
    
    
