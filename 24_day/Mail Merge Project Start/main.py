#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

used_names = []
# Create a list of the invited names
with open("Input/Names/invited_names.txt") as list_names:
    for name in list_names:
        used_names.append(name)

# Replace the "[name]" by the invited names
def replace_names(list_names):
    with open("Input/Letters/starting_letter.txt") as file:
        content = file.read()
        for names in list_names:
            replaced_file = content.replace("[name]", names.strip())
            create_letter(replaced_file,names)
            print(replaced_file)
    return replaced_file

# Create file ready to send
def create_letter(new_file,name):
    with open(f"Output/ReadyToSend/letter_for_{name}", "w") as invitation:
        invitation.write(new_file)

replace_names(used_names)



