class Solution {
    public boolean hasAllCodes(String s, int k) {
        if(k > s.length()) return false;

        double TOTAL = Math.pow(2, k);
        Map<String, Integer> map = new HashMap<>();
        int left = 0, right = k-1;

        while(right < s.length()){
            map.put(s.substring(left, right+1), map.getOrDefault(s.substring(left, right+1), 0) + 1);
            left++;
            right++;
        }

        return (double)(map.size())==TOTAL;
    }
}