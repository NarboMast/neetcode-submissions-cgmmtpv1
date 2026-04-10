class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for(String s : strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            List<String> val = anagrams.getOrDefault(new String(chars), new ArrayList<>());

            val.add(s);

            anagrams.put(new String(chars), val);
        }

        List<List<String>> res = new ArrayList<>();

        for(String key : anagrams.keySet())
            res.add(anagrams.get(key));

        return res;
    }
}
