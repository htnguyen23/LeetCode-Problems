class Solution {
    public int[] shuffle(int[] nums, int n) {
        // n is pivot point        
        // return array populated from x and y
        int [] arrRet = new int[2*n];
        int iarr = 0;
        int iXY = 0;
        while (iarr < (2*n)) {
            // array x
            arrRet[iarr] = nums[iXY];
            iarr++;
            // array y
            arrRet[iarr] = nums[iXY+n];
            iarr++;
            iXY++;
        }
        return arrRet;
    }
}