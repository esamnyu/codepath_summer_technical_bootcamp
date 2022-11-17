# Problem 1089 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        hasDupe = False 
        length_arr =len(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                if hasDupe:
                    hasDupe = False
                    continue
                else:
                    arr.insert(i, 0)
                    arr.pop(length_arr)
                    hasDupe = True
                    
       
        
