
//使用大数组与 Arrays.copyOf的快捷方法
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        int[] arr = new int[1001];
        int[] result = new int[Math.max(nums1.length,nums2.length)];
        int count = 0;
        for(int i = 0; i < nums1.length; i++){
            if(arr[nums1[i]] == 0){
                arr[nums1[i]]++;
            }
        }
        int j=0;
        for(int i=0; i<nums2.length;i++){
            if(arr[nums2[i]]==1){
                result[j++]=nums2[i];
                count++;
                arr[nums2[i]]--;
            }
        }
        return Arrays.copyOf(result,count);
    }
}