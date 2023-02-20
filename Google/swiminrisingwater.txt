class Solution {
    public int swimInWater(int[][] grid) {
        int left = grid[grid.length-1][grid.length-1];
        int right = grid.length*grid.length;
        int mid = 0;
        while (left < right){
            mid = (int)Math.floor((right+left)/2); //middle value
            int[][] g1 = new int[grid.length][grid.length];
            for (int i = 0; i < g1.length; i++){
                g1[i] = grid[i].clone();
            }
            if (canFinish(g1, mid, 0, 0)){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        return left;
    }

    public boolean canFinish(int[][] g, int t, int x, int y){
        if (x >= g.length || y >= g.length || x < 0 || y < 0){
            return false;
        }
        if (g[x][y] > t){
            return false;
        }
        if (x == g.length-1 && y == g.length-1){
            return true;
        }

        g[x][y] = t+1;
        // ^^ make sure we don't travel to this square again

        if (canFinish(g,t,x+1,y)){ //move right
            return true;
        }
        if (canFinish(g,t,x,y+1)){ //move down
            return true;
        }
        if (canFinish(g,t,x-1,y)){ //move left
            return true;
        }
        if (canFinish(g,t,x,y-1)){ //move up
            return true;
        }
        return false;
    }
}