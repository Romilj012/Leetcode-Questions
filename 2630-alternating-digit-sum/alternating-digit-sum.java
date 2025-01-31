class Solution {
    public int alternateDigitSum(int n) {
        int sum = 0;
        int sign = 1;
        String numStr = Integer.toString(n);
        for(int i = 0; i < numStr.length(); i++){
            int digit = numStr.charAt(i) - '0';
            sum += sign * digit;
            sign *= -1;
        }
        return sum;
    }
}

