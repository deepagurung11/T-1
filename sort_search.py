def bubble_sort_2d(arr):
    n = len(arr)  # number of rows in the 2d array
    m = len(arr[0])# number of columns in the 2d array; assumes all rows have equal length
    total_elements = n * m # total number of elements in the 2d array

    for i in range(total_elements - 1):
        # outer loop: goes through all elements in the 2d array

        for j in range(total_elements - 1 - i):
            # inner loop: goes through the elements, reducing the comparison range each time

            # calculate current position in 2d terms
            row1 = j//m
            col1 = j%m

            # calculate current next position (right next to current position) 
            row2 = (j+1)//m
            col2 = (j+1)%m

            # compare and possibly swap elements
            if arr[row1][col1] > arr[row2][col2]:
                # if the current element is greater than the next, swap them
                arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]

def search_element(arr, element):
    found = False # initialize a flag to track if the element is found
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                print(f"Element found at position: row = {i}, column = {j}")
                found = True
                return # Exit the function after finding the element
    if not found:
        print("Element not found in the given array.")

# example usage:
arr = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
] 

print(arr)
bubble_sort_2d(arr)
print(arr)

# searching foe an element
search = int(input("Enter the element to search: "))
search_element(arr, search)
