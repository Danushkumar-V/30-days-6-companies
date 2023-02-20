class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int ans = 0;
        int len = points.length;

        for(int i=0; i<len; i++){
            // map to store the distance
            Map<Integer, Integer> map = new HashMap<>();
            for(int j=0; j<len; j++){
                if(i != j){
                    int distance = distanceSquare(points[i], points[j]);
                    map.put(distance, map.getOrDefault(distance, 0) + 1);
                }
            }
            // traversing the map 
            for(int key: map.keySet()){
                // check discussion, there will be lot of pairs of boomerangs
                // try it with example where 4 points are at same distance with 1 point
                // it'll be clear when we make diagram
                ans += map.get(key) * (map.get(key)-1);
            }
        }

        return ans;
    }

    // This method calculates the distance between two points and returns its square
    private int distanceSquare(int[] a, int[] b){
        // We use the mathematical formula to calculate the distance between the points
        int dx = a[0] - b[0];
        int dy = a[1] - b[1];
        return dx*dx + dy*dy;
    }
}
