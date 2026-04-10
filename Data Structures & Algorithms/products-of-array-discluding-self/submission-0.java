class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        int prod = 1;
        int countZero = 0;

        for(int num : nums){
            if(num == 0){
                countZero++;
            } else {
                prod *= num;
            }
        }

        if(countZero > 1)
            return res;

        if(countZero == 1){
            for(int i = 0; i < res.length; i++){
                if(nums[i] == 0)
                    res[i] = prod;
            }
        } else {
            for(int i = 0; i < res.length; i++){
                res[i] = prod / nums[i];
            }
        }

        return res;
    }
}  
