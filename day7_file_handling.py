def write_notes():
  with open("notes.txt", "a") as file:
      note = input("Write your note: ")
      file.write(note + "\n")
      print("Note saved!")

def read_notes():
  try:
      with open("notes.txt", "r") as file:
          print("\nYour saved notes:")
          print(file.read())
  except FileNotFoundError:
      print("No notes found yet. Start by writing one!")

def main():
  print("Welcome to Notes Manager 🧠")
  while True:
      choice = input("\nWhat do you want to do?\n1. Write a note\n2. Read all notes\n3. Exit\nEnter choice (1/2/3): ")

      if choice == "1":
          write_notes()
      elif choice == "2":
          read_notes()
      elif choice == "3":
          print("Goodbye! 🖐️")
          break
      else:
          print("Invalid choice. Try again.")

main()