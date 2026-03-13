class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num *= -1
            a = list(str(num))
            a.sort(reverse=True)
            a = "-"+str(''.join(a))
            return int(a)
        a = list(str(num))
        a.sort()
        for i in range(0,len(a)):
            if(a[i] != '0'):
                a[0],a[i] = a[i],a[0]
                break
        return int(''.join(a))
                
