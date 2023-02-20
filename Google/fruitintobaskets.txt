class Solution {
    public int totalFruit(int[] fruits) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int startIndex = 0; 
        int endIndex = 0;
        int maxTotal = 1; 
        
        map.put(fruits[0], 1);
        for(int i=1; i<fruits.length; i++){
            map.put(fruits[i], map.getOrDefault(fruits[i], 0) + 1);
            endIndex++; 
            
            if(map.size() <= 2){
                maxTotal = Math.max(maxTotal, endIndex-startIndex+1); 
            } else{
                int temp = map.get(fruits[startIndex]); 
                if(temp <= 1 ) map.remove(fruits[startIndex]); 
                else map.put(fruits[startIndex], temp - 1);
                
                startIndex++; 
            } 
        }
        
        return maxTotal;
        
    }
}