class Solution {
    public boolean increasingTriplet(int[] nums) {
        int len = nums.length;
        // len is less than 3, so no triplet is poossible
        if(len<3) return false;

        // taking 2 variables low and mid and updating them regularly
        // we basically take low, mid and high and keep checking them
        // in if and else if statements
        int low = Integer.MAX_VALUE;
        int mid = Integer.MAX_VALUE;

        for(int num: nums){
            if(num <= low){
                low = num;
            } else if(num <= mid){
                mid = num;
            } else {
                return true;
            }
        }

        return false;
    }
}