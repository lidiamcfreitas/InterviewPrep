# input a vector return it in reverse order


def main():
    array = [int(x) for x in input().strip().split()]
    print(array)
    print(inverted_insertion_sort(array))


def inverted_insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]

        i = j - 1
        while i > -1 and key > array[i]:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


if __name__ == '__main__':
    main()