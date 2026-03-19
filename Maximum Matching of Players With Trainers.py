class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p1,p2 = 0,0
        players.sort()
        trainers.sort()
        ans = 0
        while p1 < len(players):
            while p2 < len(trainers) and trainers[p2] < players[p1]:
                p2 += 1
            if p2 >= len(trainers):
                break
            ans += 1
            p1 += 1
            p2 += 1
        return ans
