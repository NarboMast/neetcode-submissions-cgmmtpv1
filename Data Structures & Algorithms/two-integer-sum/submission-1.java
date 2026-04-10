class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> checked = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int curr = nums[i];

            if(checked.containsKey(curr)){
                return new int[] {checked.get(curr), i};
            } else {
                checked.put(target - curr, i);
            }
        }

        return null;
    }
}
