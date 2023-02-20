class Solution {
  // solve using kmp algo
    public String longestPrefix(String s) {
        int len = s.length();
        int[] kmp = new int[len];
        int i = 0, j = 1;
        
        while(j<len){
            char ch1 = s.charAt(i), ch2 = s.charAt(j);
            if(ch1==ch2){
                kmp[j] = i+1;
                i++;
                j++;
            } else {
                if(i==0){
                    j++;
                } else {
                    i = kmp[i-1];
                }
            }
        }
        return s.substring(0, i);
    }
}
