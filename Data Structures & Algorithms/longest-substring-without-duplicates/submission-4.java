class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;

        Set<Character> streak = new HashSet<>();

        int l = 0;
        int r = 0;

        while(r < s.length()){
            char currChar = s.charAt(r);

            if(streak.contains(currChar)){
                res = Math.max(res, r - l);
                
                streak.remove(s.charAt(l));
                l++;
            } else {
                streak.add(currChar);
                r++;
            }
        }

        return Math.max(res, streak.size());
    }
}
