class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        ans = 1
        for i in range(len(tmp)):
            if tmp[i] != tmp[len(tmp) - 1 - i]:
                ans = 0
        if(ans == 1):
            return True
        else:
            return False
