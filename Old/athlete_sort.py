


def main():
    
    my_input = input()
    my_input = my_input.split(' ')

    N = int(my_input[0])
    M = int(my_input[1])

    list_of_tuples = []
    temp = ''
    for i in range(N+1):
        temp = input().split(' ')
        if len(temp) == 1:
            break
        data = tuple(temp)
        list_of_tuples.append(data)

    K = int(temp[0])
    list_of_tuples.sort(key=lambda x: int(x[K]))

    for item in list_of_tuples:
        for element in item:
            print(element,end=' ')
        print()

    return



if __name__ == "__main__":
    main()