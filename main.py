import subprocess
import platform
import socket
import time
import os
import psutil
import colorama
from colorama import *
import difflib
import pathlib
import calendar
import datetime
import urllib.request
from PIL import Image, ImageFilter
from decimal import Decimal
import random
import string
import gzip

os.system('cls' if platform.system().lower() == 'windows' else 'clear')
today = datetime.datetime.now()
yy = today.year
mm = today.month
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "
PIPE = "│"
ELBOW = "└──"
TEE = "├──"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
colorama.init()


def encrypt_text(text):
    chars = string.punctuation + string.digits + string.ascii_letters + " "
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    cipher_text = ""
    for letter in text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # If the character is not in the chars list, leave it unchanged
    return cipher_text


def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)


def decorrupt_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
            with open(output_file, 'wb') as fw:
                fw.write(data)
        print("File successfully decorrupted.")
    except Exception as e:
        print("Error occurred while decorrupting file:", e)


print(Fore.LIGHTGREEN_EX + "ACL TERMINAL [VERSION 0.05]" + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + "(c) ACL COMPUTERS. ALL RIGHTS RESERVED.")
print("                                       ")

while True:
    print()
    cmd = input(Fore.CYAN + host_name + " " + Fore.LIGHTYELLOW_EX + " " + "~").lower().strip()

    if cmd == "ping":
        host = input(Fore.BLUE + "Enter Website To Ping: ")
        number = input(Fore.BLUE + "Enter How Many Times To Ping")


        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            print(Fore.WHITE + str(subprocess.call(command)))


        print(ping(host))

    elif cmd == 'local':
        pid = str(os.getpid())
        print(Fore.WHITE + "LOCAL IPS:" + host_ip)
        print(Fore.WHITE + "DESKTOP NAME:" + host_name)
        print(Fore.WHITE + "OS NAME:" + platform.platform())
        print(Fore.WHITE + "OS VERSION:" + platform.version())
        print(Fore.WHITE + "COMPUTER PROCESSOR:" + platform.processor())
        print(Fore.WHITE + "MACHINE:" + platform.machine())
        print(Fore.WHITE + "OS RELEASE:" + platform.release())
        print(Fore.WHITE + "REGISTERED OWNER:" + os.getlogin())
        print(Fore.WHITE + "PRODUCT ID:" + pid)
        print(Fore.WHITE + "TIME ZONE:" + time.strftime("%z", time.gmtime()))
        last_reboot = int(psutil.boot_time())
        print(Fore.WHITE + str(datetime.datetime.fromtimestamp(last_reboot)))

    elif cmd == 'date':
        print(Fore.WHITE + "DATE:" + time.strftime("%m/%d/%Y"))

    elif cmd == "list":
        try:
            dir_path = input("Enter a path: ")
            if not os.path.isdir(dir_path):
                raise FileNotFoundError
            print(Fore.WHITE + "YOUR FILES AND DIRECTORIES:")
            with os.scandir(dir_path) as entries:
                for entry in entries:
                    print(Fore.WHITE, entry.name)
        except FileNotFoundError:
            print(Fore.RED + "Error: Directory not found.")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "read":
        try:
            text = input(Fore.BLUE + "ENTER THE TEXT FILE YOU WANT TO READ")
            with open(text, 'r') as file:
                read = file.readlines()
                print(Fore.WHITE, read)
        except FileNotFoundError:
            print(Fore.RED + "Error: File not found.")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "read -c":
        try:
            print(Fore.BLUE + "ENTER THE FILE YOU WANT TO CHANGE: ")
            text1 = input(Fore.BLUE + ":")
            opeeen = open(text1, 'r+')
            print(Fore.BLUE + "RE-WRITE YOUR FILE:")
            ab = input(Fore.BLUE + ":")
            change = opeeen.write(ab)
            opeeen.close()
            print(Fore.WHITE + "file successfully updated")
        except FileNotFoundError:
            print(Fore.RED + "ERROR: FILE NOT FOUND")
        except Exception as e:
            print(Fore.RED + f"ERROR: {e}")

    elif cmd == "file_opener":
        try:
            print(Fore.BLUE + "Enter the path to the app:")
            dir = input(Fore.BLUE + ":")
            subprocess.Popen(["open", dir] if platform.system().lower() == "darwin" else ["start", dir], shell=True)
            print(Fore.WHITE + dir + " IS SUCCESSFULLY OPENED")
        except FileNotFoundError:
            print(Fore.RED + "ERROR: FILE NOT FOUND")

    elif cmd == "usage":
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory())
        print(Fore.WHITE + "CPU USAGE: " + cpu + " percent")
        print(Fore.WHITE + "RAM USAGE: " + ram)

    elif cmd == "help":
        print(Fore.WHITE + "local: Shows information about the computer")
        print(
            Fore.WHITE + "ping: sends one datagram per second and prints one line of output for every response received")
        print(Fore.WHITE + "read: Reads a text file")
        print(Fore.WHITE + "read -c: Re-writes or writes a text file")
        print(Fore.WHITE + "list: lists files and directories")
        print(Fore.WHITE + "file_opener: Allows user to open a file")
        print(Fore.WHITE + "exit: exits terminal")
        print(Fore.WHITE + "usage: shows RAM and CPU usage")
        print(Fore.WHITE + "new-file: Creates a new file")
        print(Fore.WHITE + "del: deletes a file")
        print(Fore.WHITE + "tasklist: Shows a list of taks the computer is doing")
        print(Fore.WHITE + "file_compare: compares 2 files")
        print(Fore.WHITE + "file_tree: generates a file tree")
        print(Fore.WHITE + "ren:renames a file")
        print(Fore.WHITE + "cal: shows calendar")
        print(Fore.WHITE + "search: searchs files")
        print(Fore.WHITE + "clr:cleares the screen")
        print(Fore.WHITE + "file_info: finds information about a file")
        print(Fore.WHITE + "dweb: downloads files from the internet")
        print(Fore.WHITE + "imgoptf: enchances image quality")
        print(Fore.WHITE + "math: does math")
        print(Fore.WHITE + "python:Allows you to execute python file withing terminal")
        print(Fore.WHITE + "stoptask: stops a running process or application")
        print(Fore.WHITE + "encrypt: Encrypts file or piece of text")
        print(Fore.WHITE + "compress: compresses files")

    elif cmd == "exit":
        exit()

    elif cmd == "new-file":
        newfile = input(Fore.BLUE + "NAME OF THE FILE THAT YOU WILL CREATE:")
        newpath = input("Enter your path to the file")
        filepath = os.path.join(newpath, newfile)
        ab = open(filepath, "x")
        print(Fore.WHITE + "new file created")

    elif cmd == "del":
        try:
            removefile = input(Fore.BLUE + "Enter the file you want to delete: ")

            if os.path.exists(removefile):
                os.remove(removefile)
                print(Fore.WHITE + "File deleted")
            else:
                print(Fore.RED + "File does not exist")

        except Exception as e:
            print(Fore.RED + "An error occurred:", str(e))

    elif cmd == "tasklist":
        if platform.system().lower() == "windows":
            output = os.popen('tasklist').read()
        else:
            output = os.popen('ps -eo comm,pid').read()
        print(Fore.WHITE + output)

    elif cmd == "file_compare":
        try:
            x = input(Fore.BLUE + "First File:")
            y = input(Fore.BLUE + "Second File:")
            with open(x) as file1, open(y) as file2:
                file1_text = file1.readlines()
                file2_text = file2.readlines()
            for line in difflib.unified_diff(file1_text, file2_text, fromfile=x, tofile=y, lineterm=''):
                print(Fore.WHITE + line)
        except FileNotFoundError as e:
            print(Fore.RED + f"Error: {e.filename} not found")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "file_tree":
        def generate_directory(tree, item, index, len_diritems, prefix, connector):
            tree.append(f"{prefix}{connector} {item.name}{os.sep}")
            if index != len_diritems - 1:
                prefix += PIPE_PREFIX
            else:
                prefix += SPACE_PREFIX
            add_body(tree, item, prefix)
            tree.append(prefix.rstrip())


        def add_root(tree, root_directory):
            tree.append(f"{root_directory.name}{os.sep}")
            tree.append(PIPE)


        def add_body(tree, root_directory, prefix=""):
            dir_iter = root_directory.iterdir()
            diretory_items = sorted(dir_iter, key=lambda item: item.is_file())
            len_diritems = len(diretory_items)
            for index, item in enumerate(diretory_items):
                connector = ELBOW if index == len_diritems - 1 else TEE
                if item.is_dir():
                    generate_directory(tree, item, index, len_diritems, prefix, connector)
                else:
                    tree.append(f"{prefix}{connector} {item.name}")


        def make_tree(root_directory):
            tree = []
            add_root(tree, root_directory)
            add_body(tree, root_directory)
            return tree


        try:
            directory = input("Enter a path: ")
            root_directory = pathlib.Path(directory)
            if not root_directory.is_dir():
                raise ValueError(f"{root_directory} is not a directory.")
            tree = make_tree(root_directory)
            for item in tree:
                print(item)
        except ValueError as e:
            print(Fore.RED + f"Error: {str(e)}")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "ren":
        try:
            new_address = input(Fore.BLUE + "Source address of the file:")
            new_dest = input(Fore.BLUE + "Destination of the file with the new name")
            os.rename(new_address, new_dest)  # renames and puts it in a new destination
            print(Fore.WHITE + "FILE SUCCESSFULLY RENAMED")
        except FileNotFoundError:
            print(Fore.RED + "Error: Could not find file")

    elif cmd == "cal":
        print(Fore.WHITE + calendar.month(yy, mm))

    elif cmd == "search":
        rootDir = input(Fore.BLUE + "Path of the file you want to search: ").strip()
        fileToSearch = input(Fore.BLUE + "Name of the file: ").strip()

        found = False
        for relpath, dirs, files in os.walk(rootDir):
            if fileToSearch in files:
                found = True
                print(f"File {fileToSearch} found at {relpath}")
        if not found:
            print(Fore.RED + f"File {fileToSearch} not found")

    elif cmd == "clr":
        os.system('cls' if platform.system().lower() == 'windows' else 'clear')

    elif cmd == "file_info":
        file_path = input(Fore.BLUE + "Enter file path: ")
        try:
            if os.path.exists(file_path):
                stat = os.stat(file_path)
                print(Fore.WHITE + f"File Size: {stat.st_size} bytes")
                print(Fore.WHITE + f"Last Modified: {time.ctime(stat.st_mtime)}")
                print(Fore.WHITE + f"Created: {time.ctime(stat.st_ctime)}")
                print(Fore.WHITE + f"Last Accessed: {time.ctime(stat.st_atime)}")
            else:
                print(Fore.RED + f"File {file_path} does not exist.")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "dweb":
        url = input(Fore.BLUE + "Enter URL: ")
        filename = input(Fore.BLUE + "Enter filename to save as: ")
        try:
            urllib.request.urlretrieve(url, filename)
            print(Fore.WHITE + f"File successfully downloaded as {filename}")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "imgoptf":
        img_path = input(Fore.BLUE + "Enter image path: ")
        try:
            img = Image.open(img_path)
            img = img.filter(ImageFilter.EDGE_ENHANCE)  # Example filter to enhance edges
            img.show()
            new_img_path = input(Fore.BLUE + "Enter path to save enhanced image: ")
            img.save(new_img_path)
            print(Fore.WHITE + f"Enhanced image saved at {new_img_path}")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "math":
        try:
            equation = input(Fore.BLUE + "Enter math equation (e.g., 2+2): ")
            result = eval(equation)
            print(Fore.WHITE + f"Result: {result}")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "python":
        try:
            python_file = input(Fore.BLUE + "Enter python file path: ")
            subprocess.run(["python", python_file], check=True)
        except FileNotFoundError:
            print(Fore.RED + "Error: Python file not found.")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "stoptask":
        try:
            process_name = input(Fore.BLUE + "Enter process name: ")
            subprocess.run(
                ['taskkill', '/F', '/IM', process_name] if platform.system().lower() == 'windows' else ['pkill',
                                                                                                        process_name])
            print(Fore.WHITE + f"Process {process_name} successfully stopped.")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "encrypt":
        text = input(Fore.BLUE + "Enter text to encrypt: ")
        encrypted = encrypt_text(text)
        print(Fore.WHITE + f"Encrypted text: {encrypted}")

    elif cmd == "compress":
        input_file = input(Fore.BLUE + "Enter file path to compress: ")
        output_file = input(Fore.BLUE + "Enter output compressed file path: ")
        try:
            compress_file(input_file, output_file)
            print(Fore.WHITE + "File successfully compressed.")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    else:
        print(f"command {cmd} not found")
