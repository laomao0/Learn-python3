# string.split 以分隔符 分割string
# 这在读取一个文件中的一行，然后使用split读取每一列column的数据非常有用


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')  # break string with character ' '
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
