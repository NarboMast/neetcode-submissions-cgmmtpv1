class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checked = new HashSet<>();

        for(int i : nums){
            if(!checked.add(i))
                return true;
        }

        return false;
    }
}