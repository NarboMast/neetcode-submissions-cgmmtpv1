class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];

        Map<Integer, Integer> countFreq = new HashMap<>();

        for(int num : nums){
            countFreq.put(num, countFreq.getOrDefault(num, 0) + 1);
        }

        int[][] numFreq = new int[countFreq.keySet().size()][2];

        int numFreqIdx = 0;
        for(int key : countFreq.keySet()){
            numFreq[numFreqIdx][0] = key;
            numFreq[numFreqIdx][1] = countFreq.get(key);

            numFreqIdx++;
        }

        Arrays.sort(numFreq, (a, b) -> Integer.compare(b[1], a[1]));

        for(int i = 0; i < res.length; i++){
            res[i] = numFreq[i][0];
        }

        return res;
    }
}
