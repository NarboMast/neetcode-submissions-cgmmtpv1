class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for(String s : strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            String sorted = new String(chars);

            anagrams.putIfAbsent(sorted, new ArrayList<>());
            anagrams.get(sorted).add(s);
        }

        List<List<String>> res = new ArrayList<>();

        return new ArrayList<>(anagrams.values());
    }
}
