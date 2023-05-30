class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
# [0,0,0,0,0]
# 0
# [1,2,3,4,5]
# 5
# For this test case, 1 is inserted after 0 and then popped immediately, we may need a flag here 
        count = 0
        length = m+n
        # print(length)
        for i in range(length):
            # Means that the only element in nums1 is 0 
            # if m == 0:
            #     # Insert after 0 
            #     nums1.insert(i, nums2[count])
            #     # Remove 0 in the first index 
            #     nums1.pop(0)
            # Check to make sure index is within the bounds 
            if nums1[i] == 0 and count < n:
                # Insert one position before then pop 
                # nums1.insert(i-1, nums2[count])
                # nums1.pop()
                nums1[i] = nums2[count]
                count+=1
                # print(nums1)
            else:
                continue
        # Forgot to sort the first time around 
        nums1.sort()
            
       