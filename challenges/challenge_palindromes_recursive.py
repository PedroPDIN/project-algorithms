def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 1:
        return False

    size_word = len(word[low_index:high_index])
    if size_word < 1:
        return True
    else:
        return word[low_index] == word[high_index] and is_palindrome_recursive(
          word, low_index + 1, high_index - 1
        )
