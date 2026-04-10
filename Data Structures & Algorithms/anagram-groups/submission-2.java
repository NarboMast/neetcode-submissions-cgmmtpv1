class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for(String s : strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            String sorted = new String(chars);

            List<String> val = anagrams.getOrDefault(sorted, new ArrayList<>());

            val.add(s);

            anagrams.put(sorted, val);
        }

        List<List<String>> res = new ArrayList<>();

        return new ArrayList<>(anagrams.values());
    }
}
