def levenshtein(word_1, word_2):
    """Function which give you levenshtein distance"""
    f_arr = [[(i + j) if i * j == 0 else 0 for j in range(len(word_2) + 1)] \
         for i in range(len(word_1) + 1)]
    for i in range(1, len(word_1) + 1):
        for j in range(1, len(word_2) + 1):
            if word_1[i - 1] == word_2[j - 1]:
                f_arr[i][j] = f_arr[i - 1][j - 1]
            else:
                f_arr[i][j] = 1 + min(f_arr[i - 1][j], f_arr[i][j - 1], f_arr[i - 1][j - 1])
    return f_arr[len(word_1)][len(word_2)]


if __name__ == '__main__':
    levenshtein("колокол", "молоко")
