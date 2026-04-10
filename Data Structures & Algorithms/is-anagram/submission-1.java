class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        Map<Character, Integer> checked = new HashMap<>();

        for(char c : s.toCharArray()){
            checked.put(c, checked.getOrDefault(c, 0) + 1);
        }

        for(char c : t.toCharArray()){
            if(checked.containsKey(c) && checked.get(c) != 0){
                checked.put(c, checked.get(c) - 1);
            } else {
                return false;
            }
        }

        return true;
    }
}
