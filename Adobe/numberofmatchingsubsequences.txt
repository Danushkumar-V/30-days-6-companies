class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        int count = 0;
        HashMap<Character, ArrayList<Integer>> hashMap = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            if(hashMap.containsKey(s.charAt(i))){
                hashMap.get(s.charAt(i)).add(i);
            } else{
                ArrayList<Integer> list = new ArrayList<>();
                list.add(i);
                hashMap.put(s.charAt(i), list);
            }
        }

        for(String w : words){
            if(isSubseq(w, hashMap, s)) count++;
        }
        return count;
    }

    // function to check if the word is a subsequence of the given string or not
    public boolean isSubseq(String w, HashMap<Character, ArrayList<Integer>> hashMap, String s){
        int low = -1;

        for(int i = 0; i < w.length(); i++){
            if(hashMap.containsKey(w.charAt(i))){
                if(low == -1){
                    low = hashMap.get(w.charAt(i)).get(0);
                } else{
                    low = getIndex(hashMap.get(w.charAt(i)), low);
                    if(low == -1){
                        return false;
                    }
                }
            } else{
                return false;
            }
        }
        return true;
    }

    // function to find the index of character which comes after the current 
    // character's index
    private int getIndex(ArrayList<Integer> list, int low) {
        int start = 0;
        int end = list.size()-1;
        int ans = -1;

        while (start <= end){
            int mid = start + (end - start)/2;

            if(list.get(mid) > low){
                ans = list.get(mid);
                end = mid-1;
            }else {
                start = mid+1;
            }
        }

        return ans;
    }
}