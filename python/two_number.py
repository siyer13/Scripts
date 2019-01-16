class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        for i in range(len(l1)):
            l3.append(l1[i] + l2[i])
        return l3



sol = Solution()
print(sol.addTwoNumbers([2,4,3],[5,6,4,5]))
