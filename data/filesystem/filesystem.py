import os
import zipfile

ROOT_DIR = os.getcwd()

ascii = """  _    _          _ _   ______ _____ 
 | |  | |                   (_) | |  ____/ ____|
 | |__| | _____  ___ __ __ _ _| | | |__ | (___  
 |  __  |/ _ \ \/ / '__/ _` | | | |  __| \___ \ 
 | |  | |  __/>  <| | | (_| | | | | |    ____) |
 |_|  |_|\___/_/\_\_|  \__,_|_|_| |_|   |_____/ 
                                                
                                                """
print(ascii)

def list_files():
    files = os.listdir(ROOT_DIR)
    if not files:
        print("No files in the directory.")
    else:
        for file in files:
            print(file)

def create_file(filename):
    file_path = os.path.join(ROOT_DIR, filename)
    if os.path.exists(file_path):
        print(f"Error: '{filename}' already exists.")
    else:
        with open(file_path, 'w') as f:
            f.write("")
        print(f"File '{filename}' created.")

def read_file(filename):
    file_path = os.path.join(ROOT_DIR, filename)
    if not os.path.exists(file_path):
        print(f"Error: '{filename}' does not exist.")
    else:
        with open(file_path, 'r') as f:
            print(f.read())

def write_file(filename, content):
    file_path = os.path.join(ROOT_DIR, filename)
    if not os.path.exists(file_path):
        print(f"Error: '{filename}' does not exist.")
    else:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Content written to '{filename}'.")

def delete_file(filename):
    file_path = os.path.join(ROOT_DIR, filename)
    if not os.path.exists(file_path):
        print(f"Error: '{filename}' does not exist.")
    else:
        os.remove(file_path)
        print(f"File '{filename}' deleted.")

def create_hpkg(package_name, files_to_package):
    package_path = os.path.join(ROOT_DIR, package_name)
    if package_name.endswith('.hpkg'):
        if os.path.exists(package_path):
            print(f"Error: '{package_name}' already exists.")
        else:
            with zipfile.ZipFile(package_path, 'w') as hpkg:
                for file in files_to_package:
                    file_path = os.path.join(ROOT_DIR, file)
                    if os.path.exists(file_path):
                        hpkg.write(file_path, os.path.basename(file_path))
                        print(f"Added '{file}' to '{package_name}'.")
                    else:
                        print(f"Error: '{file}' does not exist.")
            print(f"Package '{package_name}' created.")
    else:
        print("Error: Package must have a .hpkg extension.")

def extract_hpkg(package_name):
    if package_name.endswith('.hpkg'):
        package_path = os.path.join(ROOT_DIR, package_name)
        if os.path.exists(package_path):
            with zipfile.ZipFile(package_path, 'r') as hpkg:
                hpkg.extractall(ROOT_DIR)
                print(f"Extracted contents of '{package_name}'.")
        else:
            print(f"Error: '{package_name}' does not exist.")
    else:
        print("Error: The file must have a .hpkg extension.")

def handle_command(command):
    parts = command.split()
    if len(parts) == 0:
        print("Invalid command.")
        return
    
    cmd = parts[0].lower()

    if cmd == "list":
        list_files()
    elif cmd == "create":
        if len(parts) < 2:
            print("Usage: create <filename>")
        else:
            create_file(parts[1])
    elif cmd == "read":
        if len(parts) < 2:
            print("Usage: read <filename>")
        else:
            read_file(parts[1])
    elif cmd == "write":
        if len(parts) < 3:
            print("Usage: write <filename> <content>")
        else:
            write_file(parts[1], " ".join(parts[2:]))
    elif cmd == "delete":
        if len(parts) < 2:
            print("Usage: delete <filename>")
        else:
            delete_file(parts[1])
    elif cmd == "createhpkg":
        if len(parts) < 3:
            print("Usage: createhpkg <package_name.hpkg> <file1 file2 ...>")
        else:
            create_hpkg(parts[1], parts[2:])
    elif cmd == "extracthpkg":
        if len(parts) < 2:
            print("Usage: extracthpkg <package_name.hpkg>")
        else:
            extract_hpkg(parts[1])
    else:
        print("Unknown command.")

def main():
    print("Hexrail File System ('exit' to exit)")
    while True:
        command = input("Hexrail> ")
        if command.lower() == "exit":
            print("Exiting Hexrail file system...")
            break
        handle_command(command)

if __name__ == "__main__":
    main()
