class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0 
        j=0
        l=len(word1)+len(word2)
        res=[]
        while (i<len(word1) and j<len(word2)):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        while (i<len(word1)):
            res.append(word1[i])
            i+=1
        while j<len(word2):
            res.append(word2[j])
            j+=1
        

        return "".join(res)