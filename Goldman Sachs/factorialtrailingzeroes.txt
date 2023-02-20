class Solution {
    public int trailingZeroes(int n) {
        int res = 0;
        // we get a 0 when we do 5*2,
        // so here we are counting number of 5's 
        // after every 5 occurences
        while(n / 5 != 0){
            res += n/5;
            n /= 5;
        }
        return res;
    }
}
