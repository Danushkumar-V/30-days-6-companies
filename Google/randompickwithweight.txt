class Solution {
    TreeMap<Integer, Integer> map = new TreeMap<>();
    int sum = 0;

    public Solution(int[] w) {
        for(int i=0; i<w.length; i++){
            sum += w[i];
            map.put(sum, i);
        }
    }
    
    public int pickIndex() {
        int random = new Random().nextInt(sum) + 1; // add 1 to include the sum itself
        return map.ceilingEntry(random).getValue();
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */