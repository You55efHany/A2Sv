class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            for j in range((len(i) + 1) // 2):
                i[j] = 1 - i[j]
                if(j != ((len(i) + 1) // 2) - 1 or len(i) % 2 == 0):
                    i[len(i) - j - 1] = 1 - i[len(i) - j - 1]
                i[j],i[len(i) - j - 1] = i[len(i) - j - 1],i[j]
        return image
