import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") # read csv file

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()} # new dict with index and row from nato data frame

def generate_phonetic():
    word = input("Enter a word: ").upper() # receive user input
    try:
        output_list = [phonetic_dict[letter] for letter in word]  # create a list with every letter in the user input s index for the nato dict
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
