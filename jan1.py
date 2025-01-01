# 1422. Maximum Score After Splitting a String

class Solution(object):
    def maxScore(self, s):
        totalOnes = s.count('1')  
        zerosCount = 0
        onesCount = 0
        bestScore = float('-inf')

        
        for i in range(len(s) - 1):  
            if s[i] == '0':
                zerosCount += 1
            else:
                onesCount += 1

            
            currentScore = zerosCount + (totalOnes - onesCount)
            bestScore = max(bestScore, currentScore)

        return bestScore            