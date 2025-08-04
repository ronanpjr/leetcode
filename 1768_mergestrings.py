class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        big = word2
        size1, size2 = len(word1), len(word2)
        new = ''
        if (len(word1) > len(word2)):
            big = word1
            
        for i in range(len(big)):
            if(i<size1):
                new = new + word1[i]
            if(i<size2):
                new = new + word2[i]

        return new
    
    
if __name__ == '__main__':
    solver = Solution()
    print(solver.mergeAlternately("abcd", "pq"))
    