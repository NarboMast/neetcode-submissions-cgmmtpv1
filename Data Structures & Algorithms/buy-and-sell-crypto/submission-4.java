class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;

        int left = 0;
        int right = 1;

        while(right < prices.length){
            if(prices[right] < prices[left]){
                left = right;
                right = left + 1;
            } else {
                int tempRes = prices[right] - prices[left];
                res = Math.max(res, tempRes);
                right++;
            }
        }

        return res;
    }
}
