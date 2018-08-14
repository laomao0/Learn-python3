import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)
ex25.print_first_word(words)

# 关于python函数参数传递的问题
# http://winterttr.me/2015/10/24/python-passing-arguments-as-value-or-reference/
# List是可变量，所以类似于引用传递
# 在python中，strings, tuples, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象