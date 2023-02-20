class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int ans = 0;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1){
                    ans = Math.max(ans, traverse(i, j, m, n, grid));
                }
            }
        }

        return ans;
    }

    private int traverse(int i, int j, int m, int n, int[][] grid){
        if(i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == 0) return 0;

        grid[i][j] = 0;
        return 1 + traverse(i-1, j, m, n, grid) + traverse(i, j-1, m, n, grid) + traverse(i+1, j, m, n, grid) + traverse(i, j+1, m, n, grid);
    }
}