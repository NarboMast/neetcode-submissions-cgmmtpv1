class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int res = 0;

        int[][] pair = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }
        Arrays.sort(pair, (a, b) -> Integer.compare(b[0], a[0]));

        double prev = 0;
        for(int i = 0; i < pair.length; i++){
            int pos = pair[i][0];
            int sp = pair[i][1];

            double temp = (double) (target - pos) / sp;

            System.out.println("Pos: " + pos + " Sp: " + sp + " Temp: " + temp + " Prev: " + prev);

            if(temp > prev){
                res += 1;
                prev = temp;
            }
        }

        return res;
    }
}
