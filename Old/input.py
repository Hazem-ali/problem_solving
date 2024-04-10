



def main():
    #     1 4
    # x**3 + x**2 + x + 1
    my_input = input()
    my_input = my_input.split(' ')

    x = float(my_input[0])
    expected = float(my_input[1])
    
    expression = input()
    print(eval(expression) == expected)
    
    return 



if __name__ == "__main__":
    main()