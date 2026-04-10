class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;

        int left = 0;
        int right = 0;

        while(left < prices.length - 1){
            int tempRes = prices[right] - prices[left];

            System.out.println(left + " " + right + ". TempRes: " + tempRes);

            if(tempRes > res)
                res = tempRes;

            right++;

            if(right >= prices.length){
                left++;
                right = left + 1;
            }
        }

        return res;
    }
}
