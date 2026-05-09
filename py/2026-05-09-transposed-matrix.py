"""
Challenge: Transposed Matrix
Description: Given a matrix (an array of arrays), return the transposed version of it.
To transpose the matrix, swap the rows and columns.
A value at index [0, 1] should move to index [1, 0].
"""
def transpose(matrix):
    # Handle edge case for an empty matrix
    if not matrix or not matrix[0]:
        return []
        
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    transposed_matrix = []
    
    for col_idx in range(num_cols):
        new_row = []
        
        for row_idx in range(num_rows):
            new_row.append(matrix[row_idx][col_idx])
            
        # Add the newly constructed row to our transposed matrix
        transposed_matrix.append(new_row)
        
    return transposed_matrix
