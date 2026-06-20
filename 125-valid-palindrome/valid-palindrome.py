class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
      
        "".join(s)
        res=[]
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        i=0
        j=len(res)-1
       
        while i<j:
            if res[i]!=res[j]:
                return False
            i+=1
            j-=1
        return True
          