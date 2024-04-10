

def isEven(x) -> bool:

    try:
        x = int(x) % 2
    except:
        return False
    return (x == 0)


def main():
    data = input()

    sorted_data = sorted(data,
                         key=lambda x: (x.isnumeric(), isEven(x), x.isupper(), x))
    res = ''
    res = res.join(sorted_data)

    print(res)

    return


if __name__ == "__main__":
    main()
