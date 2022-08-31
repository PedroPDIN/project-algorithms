def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]
    left_index, right_index = 0, 0
    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    if first_string is None or second_string is None:
        return False

    lower_first_string = first_string.lower().replace(' ', '')
    lower_second_string = second_string.lower().replace(' ', '')

    array_first = list(lower_first_string)
    array_second = list(lower_second_string)

    merge_sort(array_first, 0, len(array_first))
    merge_sort(array_second, 0, len(array_second))

    return ''.join(array_first) == ''.join(array_second)
