class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int ans = 0;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]==0){ 
                    if(traverse(i, j, m, n, grid)) ans++;
                }
            }
        }
        return ans;
    }

    private boolean traverse(int i, int j, int m, int n, int[][] grid){
        if(i<0 || i>=m || j<0 || j>=n) return false;

        if(grid[i][j] == 1) return true;
        grid[i][j] = 1;

        boolean check1 = traverse(i-1, j, m, n, grid);
        boolean check2 = traverse(i, j-1, m, n, grid);
        boolean check3 = traverse(i+1, j, m, n, grid);
        boolean check4 = traverse(i, j+1, m, n, grid);

        return (check1 && check2 && check3 && check4);
    }
}