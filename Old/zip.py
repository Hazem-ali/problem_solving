
# INPUT
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86
# 91 92 83 89 90.5

# OUTPUT
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5      

def main():
    my_input = input()
    my_input = my_input.split(' ')

    # data_per_line = int(my_input[0])
    no_of_lines = int(my_input[1])

    subjects = []
    for i in range(no_of_lines):
        subject = tuple(input().split(' '))
        subjects.append(subject)
    
    zipped = list(zip(*subjects)) 
    for item in zipped:
        result = 0
        for element in item:
            result += float(element)
        print(result / no_of_lines)
    return



if __name__ == "__main__":
    main()