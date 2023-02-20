class Solution {
    public int calculateMinimumHP(int[][] A) {
        int n = A.length;
        int m = A[0].length;
        int[][] dp = new int[A.length][A[0].length];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }
        if(1-A[n-1][m-1] > 0)
            dp[n-1][m-1] = 1-A[n-1][m-1];
        else
            dp[n-1][m-1] =1;
        for (int j = m-2; j >= 0; j--) {
            if(dp[n-1][j+1]-A[n-1][j] > 0)
                dp[n-1][j] = dp[n-1][j+1]-A[n-1][j];
            else
                dp[n-1][j] =1;
        }
        for (int i = n-2; i >= 0 ; i--) {
            if(dp[i+1][m-1]-A[i][m-1] > 0)
                dp[i][m-1] = dp[i+1][m-1]-A[i][m-1];
            else
                dp[i][m-1] = 1;
        }
        int ans = life(dp, A, 0, 0);
        return ans;
    }
    
    public int life(int[][] dp, int[][] A, int i, int j){
        if(i>=A.length || j>=A[0].length) return 0;
        if(dp[i][j] == -1){
            int a1 = life(dp, A, i+1,j);
            int a2 = life(dp, A, i, j+1);
            int temp = Math.min(a1,a2) - A[i][j];
            if(temp>0){
                dp[i][j] = temp;
            }else{
                dp[i][j] = 1;
            }
        }
        return dp[i][j];
    }
}