def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        current_position = i
        while current_position > 0 and arr[current_position - 1] > current_element:
            arr[current_position] = arr[current_position - 1]
            current_position -= 1
        arr[current_position] = current_element
    return arr



    