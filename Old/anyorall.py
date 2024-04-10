input()
numbers = input().split()
print(any(j == j[::-1] for j in numbers) and all(int(i) > 0 for i in numbers))