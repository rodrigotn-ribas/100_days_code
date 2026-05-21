with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txtt", mode="w") as file:
    file.write("new text.")
