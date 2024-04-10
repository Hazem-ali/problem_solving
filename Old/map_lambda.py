

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        f0 = result[i-1]
        f1 = result[i-2]
        result.append(f0+f1)
    return result


def main():
    cube=lambda x: x**3
    n = int(input())
    fibo = fibonacci(n)
    print(list(map(cube,fibo)))
    return


if __name__ == "__main__":
    main()
