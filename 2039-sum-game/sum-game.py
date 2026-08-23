class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        sum_l = 0
        sum_r = 0
        q_l = 0
        q_r = 0

        for i in range(n / 2):
            if num[i] == '?':
                q_l += 1
            else:
                sum_l += int(num[i])

        for i in range(n / 2, n):
            if num[i] == '?':
                q_r += 1
            else:
                sum_r += int(num[i])

        if (q_l + q_r) % 2 != 0:
            return True

        diff_sum = sum_l - sum_r
        diff_q = q_r - q_l

        return diff_sum != (diff_q / 2) * 9