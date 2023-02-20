class Solution {
    public String customSortString(String order, String s) {
        // int[] s_count = new int[26];
        // int len = s.length();

        // StringBuilder sb = new StringBuilder("");
        
        // for(int i=0; i<len; i++){
        //     s_count[s.charAt(i) - 'a']++;
        // }

        // for(int i=0; i<order.length(); i++){
        //     char ch = order.charAt(i);
        //     s_count[ch - 'a']--;
        //     sb.append(ch);
        // }

        // for(int i=0; i<26; i++){
        //     while(s_count[i] > 0){
        //         sb.append((char)(i + 'a'));
        //         s_count[i]--;
        //     }
        // }

        // return sb.toString();

        Map<Character, Integer> map = new HashMap<>();
        int s_len = s.length(), o_len = order.length();

        StringBuilder ans = new StringBuilder("");

        // storing the count of every character in the hashmap
        for(int i=0; i<s_len; i++){
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for(int i=0; i<o_len; i++){
            char ch = order.charAt(i);
            if(map.containsKey(ch)){
                while(map.get(ch) > 0){
                    ans.append(ch);
                    map.put(ch, map.get(ch) - 1);
                }
            }   
        }

        for(Map.Entry<Character, Integer> entry: map.entrySet()){
            while(entry.getValue() > 0){
                ans.append(entry.getKey());
                map.put(entry.getKey(), entry.getValue() - 1);
            }
        }

        return ans.toString();
    }
}