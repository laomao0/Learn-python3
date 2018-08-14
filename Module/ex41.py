#!/usr/bin/env python3

# ex41: Learning To Speak Object Oriented

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# define a PHRASES list
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":  # whether input two arguments and the second one is "english"
    PHRASE_FIRST = True

# load up the words from the website, then combine them to a list
for word in urlopen(WORD_URL).readlines():  # open url file then read a line
    WORDS.append(
        word.strip().decode("utf-8"))  # strip() returns a copy of the string in which all chars have been stripped
    # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    # from the beginning and the end of the string
    # 在python3中用于存储、传输的数据类型是byte类型，所以urlopen得到的类型即word.strip()是byte类似，byte类型需要进行decode才能变成有意义的str类型


def convert(snippet_def, phrase_def):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet_def.count("%%%"))]

    # capitalize() It return a copy of the ssatring with only its first character capitalized.
    # The method count() returns the number of occurrences of substring sub in the range [start, end].
    # random.sample(population,k) return a k length list of unique elements chosen from the population sequence or set
    # 在这里使用了 for循环生成列表
    # 即 a = [ w[i] for w in b] 对 b中的每一个w，提取其第i个对象，生成List对象，并绑定到名称a上

    other_names = random.sample(WORDS, snippet_def.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet_def.count("@@@")):
        param_count = random.randint(1, 3)  # generate a random integer in range(1,3), may be 1,2,3
        param_names.append(', '.join(random.sample(WORDS, param_count)))  # use ',' to join str sequences

    for sentence in snippet_def, phrase_def:
        print("snippet_def:\n", snippet_def)
        print("phrase_def:\n", phrase_def)
        print("sentence:\n", sentence)
        result = sentence[:]
        print("result:\n", result)

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())  # get all the keys of list
        random.shuffle(snippets)  # random order the list

        for snippet in snippets:
            phrase = PHRASES[snippet]  # get the value of a list
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER:  %s\n\n" % answer)
except EOFError:
    print("\nBye")
