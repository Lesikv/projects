
def get_sum(one,two, delimiter = ' '):
    return str(one).upper() + str(delimiter).upper() + str(two).upper()


def main():
    print(get_sum('hello','hi'))

if __name__ == '__main__':
    main()
