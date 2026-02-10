class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for i in range(len(list1)):
            dic[list1[i]] = i
        
        mn = 10**18
        ans = list()
        for i in range(len(list2)):
            if list2[i] in dic:
                if i + dic[list2[i]] < mn:
                    ans.clear()
                    mn = i + dic[list2[i]]
                    ans.append(list2[i])
                elif i + dic[list2[i]] == mn:
                    ans.append(list2[i])
        return ans
