class Solution {
    public int[][] matrixBlockSum(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;

        int[][] ans = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                // limits for row
                int low_r = i-k;
                int high_r = i+k;
                // limits for col
                int low_c = j-k;
                int high_c = j+k;

                int value = 0;
                for(int r=low_r; r<=high_r; r++){
                    if(r>=0 && r<m){
                        for(int c=low_c; c<=high_c; c++){
                            if(c>=0 && c<n){
                                value += mat[r][c];
                            }
                        }
                    }
                }

                ans[i][j] = value;
            }
        }

        return ans;
    }
}