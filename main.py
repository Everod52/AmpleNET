from amplenet_parser import parser


def run():
    while True:
        try:
            s = input('AmpleNET>> ')
        except EOFError:
            break
        if not s:
            continue
        elif s == 'exit':
            break
        result = parser.parse(s)
        print(result)


if __name__ == '__main__':
    run()
