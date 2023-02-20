class Solution {
    public int numberOfSubstrings(String s) {
        int len = s.length();
        int ans = 0;
        int a_count = 0, b_count = 0, c_count = 0;
        int left = 0, right = 0;

        while(left<=right && right<len){
            char ch1 = s.charAt(right);
            if(ch1=='a') a_count++;
            else if(ch1=='b') b_count++;
            else c_count++;

            while(a_count>=1 && b_count>=1 && c_count>=1){
                char ch2 = s.charAt(left++);
                ans += len-right;
                if(ch2=='a') a_count--;
                else if(ch2=='b') b_count--;
                else c_count--;
            }
            right++;
        }

        return ans;
    }
}