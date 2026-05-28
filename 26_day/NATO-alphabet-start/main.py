import pandas

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv") # read csv file
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()} # new dict with index and row from nato data frame

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper() # receive user input
user_word_list = [nato_dict[letter] for letter in user_word] # create a list with every letter in the user input s index for the nato dict
print(user_word_list)
