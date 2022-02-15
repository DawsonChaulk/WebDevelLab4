def quick_notes():
    while True:
        note = input("Note: ")
        if note == "end":
            break
        else:
            write_note_to_file(note)

def write_note_to_file(note):
    with open("quick_notes.txt", "a") as file:
        file.write(note + "\n")


quick_notes()