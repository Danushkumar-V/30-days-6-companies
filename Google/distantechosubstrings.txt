class Solution {
    long[] hash;
    long[] power;
    long mod = (int)1e9 + 7;
    long radix = 256;
    void _hashing(String s, int n) {
        hash = new long[n];
        power = new long[n];
        power[0] = 1;
        for(int i = 1; i < n; i++) {
            hash[i] = (hash[i - 1] * radix + s.charAt(i)) % mod;
            power[i] = (power[i - 1] * radix) % mod;
        }
    }
    long calculateHash(int l, int r) {
        long val = (hash[r] - hash[l] * power[r - l] % mod + mod ) % mod;
        return val;
    }
    public int distinctEchoSubstrings(String text) {
        int n = text.length();
        _hashing(text, n);
        Set<Long> set = new HashSet<>();
        for(int len = 1; len <= n / 2; len++) {
            int count = 0;
            for(int i = 0, j = len; j < n; i++, j++) {
                char ci = text.charAt(i);
                char cj = text.charAt(j);
                if(ci == cj)
                    count++;
                else count = 0;
                if(count == len){
                    long _hash = calculateHash(i, j);
                    set.add(_hash);
                    count--;
                }    
            }
        }
        return set.size();
    }
}
