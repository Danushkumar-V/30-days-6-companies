class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int start = -1;
        int end = n;

        int max = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            if(max < nums[i]){
                max = nums[i];
            }
            if(max > nums[i]){
                end = i;
            }
        }

        int min = Integer.MAX_VALUE;
        for(int i = n - 1; i >= 0; i--){
            if(min > nums[i]){
                min = nums[i];
            }
            if(min < nums[i]){
                start = i;
            }
        }
        if(start == -1){
            return 0;
        }
        return (end - start + 1);
    }
}