class Solution {
    public HashMap<String, Integer> sortByValue(HashMap<String, Integer> hm){
        // Create a list from elements of HashMap
        List<Map.Entry<String, Integer>> list =
            new LinkedList<Map.Entry<String, Integer>>(hm.entrySet());

        // Sort the list
        Collections.sort(list, new Comparator<Map.Entry<String, Integer> >() {
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2)
            {
                //if frequency is same compare by keys and sort lexicographically
                if((o2.getValue()).compareTo(o1.getValue())==0){
                    return (o1.getKey()).compareTo(o2.getKey());
                }
                //else sort by frequency using values
                return (o2.getValue()).compareTo(o1.getValue());
            }
        });
        
        // put data from sorted list to hashmap 
        HashMap<String, Integer> temp = new LinkedHashMap<String, Integer>();
        for (Map.Entry<String, Integer> aa : list) {
            temp.put(aa.getKey(), aa.getValue());
        }
        return temp;
    }

    public List<String> topKFrequent(String[] words, int k) {
        List<String> ans = new ArrayList<>();
        HashMap<String , Integer> mp = new HashMap<>();
        // make key value pair using hashmap
        for(int i=0;i<words.length;i++){
            mp.put(words[i],mp.getOrDefault(words[i],0)+1);
        }
        HashMap<String , Integer> map = sortByValue(mp);// the function will return required sorted map
        //System.out.print(map);
        
        int x=0;
        for(String str : map.keySet()){
            if(x==k){
                break;
            }
            ans.add(str);// adding topkfrequent items
            x++;
        }
        return ans;
    }
}