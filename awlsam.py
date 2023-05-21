import pyreadline
import os


def save_file(filepath, content):
    directory = os.path.dirname(filepath)
    os.makedirs(directory, exist_ok=True)

    with open(filepath, 'w') as file:
        file.write(content)
    print(f"Saved '{filepath}' successfully!")


def open_file(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        print(f"Opened '{filepath}':\n{content}")
        return content
    else:
        print(f"File '{filepath}' not found.")
        return ""


def main():
    print(" Awlsam Code Editor")
    print("--------------------")
    filename = input("Enter filename: ")
    path = input("Enter path: ")
    filepath = os.path.join(path, filename)

    choice = input("Choose an option: (C)reate new file or (O)pen existing file: ").lower()
    if choice == "c":
        print("Creating a new file...")
        content = ""
    elif choice == "o":
        content = open_file(filepath)
    else:
        print("Invalid choice. Exiting...")
        return

    pyreadline.Readline().startup_hook = lambda: pyreadline.Readline().insert_text(content)

    try:
        while True:
            line = input()
            if line == ":w":
                save_file(filepath, content)
                break
            else:
                content += line + "\n"
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
