#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = '[name]'

with open("./Input/Letters/starting_letter.txt") as data:
    starting_letter = data.read()


with open("./Input/Names/invited_names.txt") as data:
    names = data.read().split()


print(names)

for name in names:
    name_letter = starting_letter.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as data:
        data.write(name_letter)