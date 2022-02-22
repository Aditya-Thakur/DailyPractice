package q1;

class Solution {
    public static int removeDuplicates(int[] nums) {
        int counter = 1;
        int current = nums[0];
        for(int i=1; i< nums.length; i++) {
            counter++;
            if(current==nums[i]) {
                counter--;
            } else {
                nums[counter-1]=nums[i];  
                current = nums[i];
            }
        }
        return counter;
    }
}