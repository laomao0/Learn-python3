FILE_PATH = 'new_file.txt'
OUT_PATH = 'out_file.txt'

# 在 python2 中，字符串有两个类型，一个是unicode，一个是str，前者表示文本字符串，后者表示字节序列，不过两者没有明显的界限
# 在 python3 中，做了严格的区分，分别使用str表示字符串，byte表示字节序列，任何需要写入文本或者网络传输的数据只接受字节序列
#    py2       py3     表现      转换       作用
#   str       byte     字节      encode    存储、传输
#   unicode   str      字符      decode     展示

# 所以在python3 中 一般的string类型需要进行 encode，即encode（utf_string） ->> byte

def main():
    all_data = []
    with open(FILE_PATH, 'rb') as f, open(OUT_PATH, 'wb') as mf:
        for line in f:
            parse = line.split(','.encode())
            p1 = parse[0]
            all_data.append(p1)
            p1_1 = int(p1)
            mf.write((str(p1_1) + '\n').encode())  # write() 方法用于向文件中写入指定字符串


if __name__ == '__main__':
    main()
