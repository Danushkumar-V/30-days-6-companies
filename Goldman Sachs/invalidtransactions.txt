class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        List<String> ans = new ArrayList<>();
        
        for(int i=0; i<transactions.length; i++){
            String[] temp1 = transactions[i].split(",");

            // if current transactions's value > 1000
            if(Integer.parseInt(temp1[2]) > 1000){
                ans.add(transactions[i]);
                continue;
            }

            // checking for every other transaction with the current transaction
            for(int j=0; j<transactions.length; j++){
                if(i != j){
                    String[] temp2 = transactions[j].split(",");

                    // checking if both have same name
                    if(temp1[0].equals(temp2[0])){
                        // checking for both time and place condition together
                        if(Math.abs(Integer.parseInt(temp1[1]) - Integer.parseInt(temp2[1])) <= 60 && !temp1[3].equals(temp2[3])){
                            ans.add(transactions[i]);
                            break;
                        }
                    }
                }
            }
        }
        return ans;
    }
}
