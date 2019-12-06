def read_file(file_name):
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
        result = ''.join(lines)
        return result


if __name__ == '__main__':
    print(read_file('test.txt'))
