class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        
        int m = 1000000007;
        long ans = 0;
        
        // It represnts the timelime
        // i.e. for how many days a person will remember the 
        // secret and then forget
        int[] dayTracker = new int[forget];
        
        // Initialze (at 1st day 1 person knows)
        dayTracker[0] = 1;
        
        for(int day = 2; day <= n ; day++){
            // Increase discovery day for everyone
            for(int i = forget - 1; i > 0 ; i--){
                dayTracker[i] = dayTracker[i-1]; 
            }
            dayTracker[0] = 0;
            
            // Share secret
            for(int i = delay; i < forget ; i++){
                dayTracker[0] = (dayTracker[0]+dayTracker[i]) % m;
            }
        }
        
        // Find total peoples
        for(int i  = 0; i < forget ; i++){
            ans+= dayTracker[i];
        }
        
        return (int)(ans % m);
    }
}
