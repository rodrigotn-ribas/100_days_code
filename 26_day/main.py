with open("file1.txt") as f1:
    f1_list = f1.read().split()
    f1_list = [int(number) for number in f1_list]
    print(f1_list)


with open("file2.txt") as f2:
    f2_list = f2.read().split()
    f2_list = [int(number) for number in f2_list]
    print(f2_list)

equal_number = []

for i in f1_list:
    for j in f2_list:
        if i == j and i not in equal_number:
            equal_number.append(i)


print(equal_number)



# percorrer as duas listas com um for. para cada item de uma lista, verifique a lista 2 inteira