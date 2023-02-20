class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        int max = Integer.MIN_VALUE;

        if(n<=2){
            return n;
        }

        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++){
                int total = 2;
                
                int x1 = points[i][0];
                int x2 = points[j][0];
                int y1 = points[i][1];
                int y2 = points[j][1];    
                
                for(int k=0; k<n && k != i && k != j; k++){
                    int x = points[k][0];
                    int y = points[k][1];
                    if((y2 - y1)*(x - x1) == (x2 - x1)*(y - y1) ){
                        total++;
                    }
                }
                max = Math.max(max, total);
            }
        }  
        return max;
    }
}
