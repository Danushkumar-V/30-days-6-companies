class Solution:
    def longestPrefix(self, s: str) -> str:
        l = 0
        lps = [0]
        
        i = 1
        while i < len(s):
            if(s[i] == s[l]):
                l+=1
                lps.append(l)
                i+=1
            else:
                if(l != 0):
                    l = lps[l - 1]      
                else:
                    lps.append(0)
                    i+=1
        n = lps[len(lps) - 1]
        return s[0:n]   