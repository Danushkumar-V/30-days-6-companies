/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray arr) {
        int low = 0, high = arr.length() - 1;

        while(low <= high){
            int mid = low + (high-low) / 2;

            if(arr.get(mid) < arr.get(mid+1) && arr.get(mid) < target){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        if(arr.get(low) == target) return low;
        high = arr.length() - 1;

        while(low <= high){
            int mid = low + (high-low) / 2;
            
            if(arr.get(mid) < arr.get(mid-1) && arr.get(mid) < target){
                high = mid - 1;
            } else{
                low = mid + 1;
            }
        }

        if(arr.get(high)==target){
            return high;
        }

        return -1;
    }
}