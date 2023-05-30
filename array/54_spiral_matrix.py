class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Instead of checking for -1 or None, we use a boolean variable instead
        # Edge case: empty matrix
        if not matrix:
            return []

        # Initialize variables to keep track of the rows and columns of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize variables to keep track of the current row and column
        row = 0
        col = 0

        # Initialize a list to store the spiral order
        spiral_order = []

        # Initialize a variable to keep track of the direction (0 = right, 1 = down, 2 = left, 3 = up)
        direction = 0

        # Initialize a copy of the matrix to track visited elements
        ref_matrix = [[False for _ in range(cols)] for _ in range(rows)]

        # Iterate until all elements have been visited
        while len(spiral_order) < rows * cols:
            # Append the current element to the spiral order
            spiral_order.append(matrix[row][col])

            # Mark the current element as visited
            ref_matrix[row][col] = True

            # Move to the next element in the current direction
            if direction == 0:  # right
                col += 1
                if col == cols or ref_matrix[row][col]:  # End of row or element has already been visited
                    direction = 1  # Change direction to down
                    col -= 1
                    row += 1
            elif direction == 1:  # down
                row += 1
                if row == rows or ref_matrix[row][col]:  # End of matrix or element has already been visited
                    direction = 2  # Change direction to left
                    row -= 1
                    col -= 1
            elif direction == 2:  # left
                col -= 1
                if col < 0 or ref_matrix[row][col]:  # Beginning of row or element has already been visited
                    direction = 3  # Change direction to up
                    col += 1
                    row -= 1
            elif direction == 3:  # up
                # After the line of code runs, the row might become negative, we account for this in the following if statement
                row -= 1
                if row < 0 or ref_matrix[row][col]:  # Beginning of matrix or element has already been visited
                    direction = 0  # Change direction to right
                    row += 1
                    col += 1

        # Return the spiral order
        return spiral_order