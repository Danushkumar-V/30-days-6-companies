class Solution {
    public int maxCoins(int[] piles) {
        // we will give the lowest number of coins to bob, hence reserve them
        // now start from ahead of those coins after sorting the array and keep 
        // adding the lower number of coins to your answer
        Arrays.sort(piles);
        int len = piles.length;
        int bob = len/3;

        int ans = 0;
        for(int i=bob; i<len; i=i+2){
            ans += piles[i];
        }
        return ans;
    }
}