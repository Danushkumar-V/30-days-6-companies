class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int len = nums.length;
        int sum = 0;
        for(int num: nums) sum+=num;

        Arrays.sort(nums);
        return helper(nums, len-1, new int[k], k, sum/k);
    }

    private boolean helper(int[] nums, int index, int[] sum, int k, int target){
        if(index==-1) return true;
        for(int i=0; i<k; i++){
            if(sum[i] + nums[index] > target || (i>0 && sum[i] == sum[i-1])) continue;

            sum[i] += nums[index];

            if(helper(nums, index-1, sum, k, target)) return true;

            sum[i] -= nums[index];
        }

        return false;
    }
}