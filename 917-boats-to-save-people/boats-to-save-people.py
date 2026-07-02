class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res=0
        left=0
        right=len(people)-1
        while left <= right:
            remain=limit-people[right]
            right-=1
            res+=1
            if left<=right and remain >=people[left]:
                left+=1
        return res


        