class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        
        combinationSum(n, k, 1, ds, ans);
        return ans;
    }
    
    private void combinationSum(int target, int numbers, int start, List<Integer> ds, List<List<Integer>> ans){
        if(ds.size() == numbers && target == 0){
            ans.add(new ArrayList<>(ds));
        }
        
        for(int i = start; i <= 9; i++){
            if(i > target) break;
            
            ds.add(i);
            combinationSum(target - i, numbers, i + 1, ds, ans);
            ds.remove(ds.size() - 1);
        }
    }
}