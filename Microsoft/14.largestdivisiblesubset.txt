class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        ArrayList<Integer> res = new ArrayList<>();
        int[] dp = new int[nums.length+1];
        Arrays.fill(dp,-1);
        solve(1,0,nums,new ArrayList<>(),res,dp);
        return res;
    }
    private void solve(int prev,int curr,int[] nums,ArrayList<Integer> currAns,ArrayList<Integer> res,int[] dp) {
        if(curr >= nums.length) {
            if(currAns.size() > res.size()) {
                res.clear();
                res.addAll(currAns);
            }
            return;
        }    
        if(dp[curr] < currAns.size() && (prev%nums[curr] ==0 || nums[curr]%prev == 0)) {
            dp[curr] = currAns.size();
            currAns.add(nums[curr]);
            solve(nums[curr],curr+1,nums,currAns,res,dp);
            currAns.remove(currAns.size()-1);
        }
        solve(prev,curr+1,nums,currAns,res,dp);
    }
}
