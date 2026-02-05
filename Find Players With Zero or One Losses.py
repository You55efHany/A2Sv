class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mp = {}
        st = set({})

        for i in range(len(matches)):
            st.add(matches[i][0])
            st.add(matches[i][1])
            
            if matches[i][1] in mp:
                mp[matches[i][1]] += 1
            else:
                mp[matches[i][1]] = 1
        
        winners = list()
        losers = list()
        for i in st:
            if i in mp:
                if mp[i] == 1:
                    losers.append(i)
            else:
                winners.append(i)
        
        losers.sort()
        winners.sort()
        return[winners,losers]
