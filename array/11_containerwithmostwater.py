class Solution:
    def maxArea(self, height: List[int]) -> int:
        # We're keeping track of two things, the maximum area, which is the distance between the start of the array and the end of the array
        # We also care about finding the tallest lines between at the edges of the array
        # Difference between startline and endline * (lesser height of the startline or endline)
        # We care about the indices and not the values here 
        start_line = 0
        end_line = len(height)-1
        shorter_line = min(start_line, end_line)
        maximum_area = -1

        while start_line < end_line: 
            # We want to move the shorter line in hopes of finding the taller line 
            # We care about the shorter line, not about the shorter indice
            shorter_line = min(height[start_line], height[end_line])
            current_area = (end_line-start_line) * shorter_line
            if current_area > maximum_area:
                maximum_area = current_area  
            # Consider using if and elif, else  
            if height[start_line] < height[end_line]:
                start_line+=1
            elif height[end_line] < height[start_line]:
                end_line-=1
            else: #height[start_line] == height[end_line]:
                # Increment the start_line or decrement the end_line 
                start_line +=1  
        return maximum_area