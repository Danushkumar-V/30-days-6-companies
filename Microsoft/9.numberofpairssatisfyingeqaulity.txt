class Solution {
    /**
        Rearrange the equation:
            nums1[i]-nums2[i] <= nums1[j]-nums2[j]+diff
        
        Step 1:
            store the left side of equation in an array list
        Step 2:
            call merge sort on the newly created list and pass diff
        Step 3:
            in the merge function check it with the right side of the equation,
            as the array is sorted the right hand side will be always greater than left
            so if we find any solution then all the elements ahead of the solution index, 
            will add to the count
        Step 4:
            after checking for index, sort the array in the merge function
     */


    long count = 0;
    public long numberOfPairs(int[] nums1, int[] nums2, int diff) {
        int len = nums1.length;

        // step1
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<len; i++){
            list.add(nums1[i]-nums2[i]);
        }

        mergeSort(list, 0, len-1, diff);
        return count;
    }
    // step2
    private void mergeSort(ArrayList<Integer> list, int start, int end, int diff){
        if(start==end) return;

        int mid = (start+end)/2;
        mergeSort(list,start,mid,diff);
        mergeSort(list,mid+1,end,diff);

        merge(list,start,mid,end,diff);
        return;
    }

    private void merge(ArrayList<Integer> list, int start, int mid, int end, int diff){
        int left = start, right = mid+1;
        // step3
        while(left<=mid && right<=end){
            if(list.get(left) <= list.get(right)+diff){
                count += end-right+1;
                left++;
            } else {
                right++;
            }
        }
        // step4
        List<Integer> sub = new ArrayList<>();
        for(int i=start; i < end+1; i++){
            sub.add(list.get(i));
        }
        Collections.sort(sub);

        for(int i=start; i < end+1; i++){
            list.set(i, sub.get(i-start));
        }
        return;
    }

}
