with open('file.txt') as f1:
    numbers1 = f1.readlines()
    int_num1 = [int(num1.strip()) for num1 in numbers1 if num1.strip().isdigit()]

with open('file2.txt') as f2:
    numbers2 = f2.readlines()
    int_num2 = [int(num2.strip()) for num2 in numbers2 if num2.strip().isdigit()]

result = [common for common in int_num1 if common in int_num2]
print(result)