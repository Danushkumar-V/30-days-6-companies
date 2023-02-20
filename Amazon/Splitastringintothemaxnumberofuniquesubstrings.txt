class Solution {
    HashSet<String> set = new HashSet<>();
    int count = 0;

    public int maxUniqueSplit(String s) {
        helper(s, 0, "");
        return count;
    }

    private void helper(String s, int index, String str){
        // base case
        if(index==s.length()){
            count = Math.max(count, set.size());
            return;
        }
        
        for(int i=index; i<s.length(); i++){
            str = s.substring(index, i+1);
            
            if(set.contains(str)) continue;

            set.add(str);
            helper(s, i+1, str);
            set.remove(str);
        }
    }
}