class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length - 1;

        while(i < j){
            int tempSum = numbers[i] + numbers[j];

            if(tempSum > target){
                j--;
            } else if (tempSum < target) {
                i++;
            } else {
                // +1 to compensate for indexing from 0 in an array
                return new int[] {i + 1, j + 1};
            }
        }

        return null;
    }
}
