class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> checked = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int curr = nums[i];

            if(checked.containsKey(curr)){
                res[0] = checked.get(curr);
                res[1] = i;
                return res;
            } else {
                checked.put(target - curr, i);
            }
        }

        return res;
    }
}
