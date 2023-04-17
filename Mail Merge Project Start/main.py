PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as invited_name:
    names = invited_name.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()
    print(letter_content)
    for name in names:
        name = name.strip("\n")
        new_letter = letter_content.replace(PLACE_HOLDER, name)
        with open(f"./Output/ReadyToSend/send_to_{name}.txt", "w") as send_letter:
            send_letter.write(new_letter)
    
