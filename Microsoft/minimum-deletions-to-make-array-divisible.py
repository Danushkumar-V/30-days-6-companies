class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        GCD = gcd(*numsDivide)
        ls = sorted(nums)
        c = 0
        for i in range(len(ls)):
            if GCD % ls[i] != 0:
                c+=1;
            else:
                return c
        return -1