import pandas
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")



nato_names = {row.letter: row.code for (index, row) in nato_file.iterrows()}
print(nato_names)

def generate_nato():
    your_name = input("what is your name:").upper()
    try:
        nato_list = [nato_names[letter] for letter in your_name]
    except KeyError:
        print("Sorry!!, Only alphabets are allowed")
        generate_nato()
    else:
        print(nato_list)

generate_nato()

