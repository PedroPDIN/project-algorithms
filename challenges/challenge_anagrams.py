def bubble_sort_first_string(array):
    size_array = len(array)
    for element in range(size_array - 1):
        for item in range(0, size_array - 1 - element):
            if array[item] > array[item + 1]:
                current_element = array[item]
                array[item] = array[item + 1]
                array[item + 1] = current_element
    return "".join(array).lower()


def bubble_sort_second_string(array):
    size_array = len(array)
    for element in range(size_array - 1):
        for item in range(0, size_array - 1 - element):
            if array[item] > array[item + 1]:
                current_element = array[item]
                array[item] = array[item + 1]
                array[item + 1] = current_element
    return "".join(array).lower()


def is_anagram(first_string, second_string):
    current_first_string = bubble_sort_first_string(list(first_string))
    current_second_string = bubble_sort_second_string(list(second_string))
    print(current_first_string)

    return current_first_string == current_second_string
  
if __name__ == '__main__':
    print(is_anagram('PEDRA', 'Perda'))
