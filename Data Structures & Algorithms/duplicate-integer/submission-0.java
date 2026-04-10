class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checked = new HashSet<>();

        for(int i : nums){
            if(checked.contains(i)){
                return true;
            } else {
                checked.add(i);
            }
        }

        return false;
    }
}