class Solution {
    public int maxConsecutive(int bottom, int top, int[] special) {
        Arrays.sort(special);
        int ans = 0;
        int maxDiff = 0;
        for(int i=0; i<special.length-1; i++){
            maxDiff = Math.max(maxDiff, special[i+1]-special[i]);
        }

        ans = Math.max(maxDiff-1, Math.max(special[0]-bottom, top-special[special.length-1]));

        return ans==1 ? 0 : ans;
    }
}