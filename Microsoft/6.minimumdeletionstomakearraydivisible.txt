class Solution {
    public int minOperations(int[] nums, int[] numsDivide) {
        Arrays.sort(nums);
        int GCD = findGcd(numsDivide, numsDivide.length);
        Arrays.sort(nums);

        for(int i=0; i<nums.length; i++){
            if(GCD % nums[i] == 0) return i;
        }

        return -1;
    }

    private int findGcd(int[] arr, int b){
        int result = arr[0];
        for (int element: arr){
            result = gcd(result, element);
            if(result == 1){
               return 1;
            }
        }
        return result;
    }

    private int gcd(int a, int b)
    {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }
}
