from collections import defaultdict, Counter
dct = defaultdict(int)


data = [{'a':5}, {'a':1}, {'b':1}, {'a':1}, {'a':1}]


def test2():
    for key in data:
        dct[key] += 1
    print(dct)


if __name__ == '__main__':
    pass