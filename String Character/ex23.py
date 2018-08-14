# DBES原则
# Decode Bytes Encode Strings
# 在 python2 中，字符串有两个类型，一个是unicode，一个是str，前者表示文本字符串，后者表示字节序列，不过两者没有明显的界限
# 在 python3 中，做了严格的区分，分别使用str表示字符串，byte表示字节序列，任何需要写入文本或者网络传输的数据只接受字节序列
#    py2       py3     表现      转换       作用
#   str       byte     字节      encode    存储、传输
#   unicode   str      字符      decode     展示

# 所以在python3 中 一般的string类型需要进行 encode，即encode（utf_string） ->> byte （即encode string, decode bytes）

# 倒入sys module
import sys

# 利用命令行参数 解析传入的指令
script, encoding, error = sys.argv


# 定义主函数main，该函数输入参数为文件，编码方法，错误类型
def main(language_file: object, encoding: object, errors: object) -> object:
    line = language_file.readline()

    if line:  # 如果读取的值不为空
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()  # 用于移除字符串头尾指定的字符（默认为空格）或字符序列
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


if __name__ == '__main__':
    languages = open("language.txt", encoding="utf-8")
    main(languages, encoding, error)
else:
    print("The module is being imported from another module")
