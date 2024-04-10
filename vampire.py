def is_vampire_num_1(num):

    num_str = str(num)
    num_len = len(num_str)

    # if num has odd number of digits -> cannot be vampire
    if num_len % 2 != 0:
        return False

    for i in range(10 ** ((num_len // 2) - 1), 10 ** ((num_len // 2) + 1)):

        # skip the number that is not divisible by num
        if num % i != 0:
            continue

        factor_1 = str(num // i)
        factor_2 = str(num // int(factor_1))
        if sorted(factor_1 + factor_2) == sorted(num_str):
            print(f"Vampire number: {num} with factors {factor_1}, {factor_2}")
            return True

    return False


def is_vampire_num_2(num):

    num_str = str(num)
    num_len = len(num_str)

    # if num has odd number of digits -> cannot be vampire
    if num_len % 2 != 0:
        return False

    for i in range(10 ** ((num_len // 2) - 1), 10 ** ((num_len // 2) + 1)):

        # skip the number that is not divisible by num
        if num % i != 0:
            continue

        factor_1 = num // i
        factor_2 = num // factor_1
        if (factor_1 * factor_2) % 9 == (factor_1 + factor_2) % 9:
            print(f"Vampire number: {num} with factors {factor_1}, {factor_2}")
            return True

    return False


def main():
    min_range = int(input("min range: "))
    max_range = int(input("max range: "))

    vampire_numbers_1 = []
    vampire_numbers_2 = []

    for num in range(min_range, max_range):
        if is_vampire_num_1(num):
            vampire_numbers_1.append(num)

    print("===============================")
    for num in range(min_range, max_range):
        if is_vampire_num_1(num):
            vampire_numbers_2.append(num)

    print(f"{vampire_numbers_1=:}")
    print(f"{vampire_numbers_2=:}")
    return 0


if __name__ == "__main__":
    main()
