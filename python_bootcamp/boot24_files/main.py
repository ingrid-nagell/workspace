placeholder = "[name]"

with open("people.txt", "r") as f:
    people = f.readlines()

with open("letter.txt") as f:
    letter = f.read()
    for name in people:
        new_name = name.strip()
        with open(f"./ready_to_send/letter_to_{new_name}.txt", mode='w') as f:
            f.write(letter.replace(placeholder, new_name))