class Solution {
    public int minimumCardPickup(int[] cards) {
        int len = cards.length;
        int ans = Integer.MAX_VALUE;

        // map to store the current card value and its index
        Map<Integer, Integer> map = new HashMap<>();   
        for(int i=0; i<len; i++){
            if(map.containsKey(cards[i])){
                ans = Math.min(ans, i - map.get(cards[i]) + 1);
            }
            // update the value of index as we are just moving forward
            map.put(cards[i], i);
        }

        return ans==Integer.MAX_VALUE ? -1 : ans;
    }
}
