class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int ans = Integer.MIN_VALUE;
        for(int l: left){
            ans = Math.max(ans, l);
        }

        for(int r: right){
            ans = Math.max(ans, n-r);
        }

        return ans;
    }
}