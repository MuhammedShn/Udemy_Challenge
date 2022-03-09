PLACE_HOLDER = "[name]"

names = []

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for index in range(len(names)):
    names[index]=names[index].strip("\n")

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        letter_contents = letter_contents.replace(PLACE_HOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready_to_send:
            ready_to_send.write(letter_contents)

