class StockPrice {
    private HashMap<Integer, Integer> timestamp_price_map;
    private PriorityQueue<int[]> minHeap;
    private PriorityQueue<int[]> maxHeap;
    
    private int latestTimeStamp = Integer.MIN_VALUE;

    public StockPrice() {
        timestamp_price_map = new HashMap<>();
        minHeap = new PriorityQueue<>((a, b) -> a[1]-b[1]);
        maxHeap = new PriorityQueue<>((a, b) -> b[1]-a[1]);
    }
    
    public void update(int timestamp, int price) {
        timestamp_price_map.put(timestamp, price);
        minHeap.add(new int[]{timestamp, price});
        maxHeap.add(new int[]{timestamp, price});

        latestTimeStamp = Math.max(latestTimeStamp, timestamp);
    }
    
    public int current() {
        return timestamp_price_map.get(latestTimeStamp);
    }
    
    public int maximum() {
        int[] max = maxHeap.peek();
        while(timestamp_price_map.get(max[0]) != max[1]){
            maxHeap.poll();
            max = maxHeap.peek();
        }

        return max[1];
    }
    
    public int minimum() {
        int[] min = minHeap.peek();
        while(timestamp_price_map.get(min[0]) != min[1]){
            minHeap.poll();
            min = minHeap.peek();
        }

        return min[1];
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */
