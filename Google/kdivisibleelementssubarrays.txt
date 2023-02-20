class Solution {
    public int countDistinct(int[] nums, int k, int p) {
        Set<String> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            int count = 0;
            StringBuilder sb = new StringBuilder();

            for (int j = i; j < nums.length; j++) {
                if (nums[j] % p == 0) count++;
                if (count > k) break;

                sb.append(nums[j] + " ");
                set.add(sb.toString());
            }
        }

        return set.size();
    }
}

// class Solution {
//     public int countDistinct(int[] nums, int k, int p) {
//         Set<List<Integer>> set = new HashSet<>();

//         for(int i=0; i<nums.length; i++){
//             int count = 0;
//             List<Integer> temp = new ArrayList<>();
//             for(int j=i; j<nums.length; j++){
//                 temp.add(nums[j]);
                
//                 if(nums[j] % p == 0) count++;
//                 if(count > k) break;

//                 set.add(temp);
//             }
//         }

//         return set.size();
//     }
// };