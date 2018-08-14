FILE_PATH = 'new_file.txt'


def main():
    all_data = []
    with open(FILE_PATH, 'r') as f:
        for line in f:
            parse = line.split(',')
            p1 = parse[0]
            p2 = parse[1]
            p3 = parse[2]
            all_data.append(p3)
    print(all_data)


if __name__ == '__main__':
    main()
