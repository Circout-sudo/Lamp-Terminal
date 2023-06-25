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
from win32api import *
import urllib.request
from PIL import Image, ImageFilter
from decimal import Decimal
os.system('cls')
today = datetime.datetime.now()
yy =  today.year
mm = today.month
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "
PIPE = "│"
ELBOW = "└──"
TEE = "├──"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
colorama.init()
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
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        newwidth = str(width)
        newheight = str(height)
        print(Fore.WHITE + "Screen resolution" + newwidth, "x", newheight)
        last_reboot = int(psutil.boot_time())
        print(Fore.WHITE + str(datetime.datetime.fromtimestamp(last_reboot)))

        def get_uptime():
            uptime_ticks = GetTickCount()
            uptime_seconds = uptime_ticks / 1000.0
            return uptime_seconds
        print(f"System uptime: {get_uptime()} seconds")

    elif cmd == 'date':
        print(Fore.WHITE + "DATE:" + time.strftime("%m/%d/%Y"))

    elif cmd == "list":
        try:
            dir_list = input("Enter a path")
            print(Fore.WHITE + "YOUR FILES AND DIRECTORIES:")
            print(Fore.WHITE, dir_list)
        except FileNotFoundError:
            print(Fore.RED + "Error: File not found.")
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
            os.startfile(dir)
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
        print(Fore.WHITE + "ping: sends one datagram per second and prints one line of output for every response received")
        print(Fore.WHITE + "read: Reads a text file")
        print(Fore.WHITE + "read -c: Re-writes or writes a text file")
        print(Fore.WHITE + "list: lists files and directories")
        print(Fore.WHITE + "file_opener: Allows user to open a file")
        print(Fore.WHITE + "exit: exits the SINO terminal")
        print(Fore.WHITE + "usage: shows RAM and CPU usage")
        print(Fore.WHITE + "new-file: Creates a new file")
        print(Fore.WHITE + "del: deletes a file")
        print(Fore.WHITE + "boottime: show the computers boottime")
        print(Fore.WHITE + "tasklist: Shows a list of taks the computer is doing")
        print(Fore.WHITE + "file_compare: compares 2 files")
        print(Fore.WHITE + "file_tree: generates a file tree")
        print(Fore.WHITE + "serial_number: shows serial number of the motherboard ")
        print(Fore.WHITE + "ren:renames a file")
        print(Fore.WHITE + "cal: shows calendar")
        print(Fore.WHITE + "search: searchs files")
        print(Fore.WHITE + "clr:cleares the screen")
        print(Fore.WHITE + "hangman: A game to play when your taking a break")
        print(Fore.WHITE + "file_info: finds information about a file")
        print(Fore.WHITE + "dweb: downloads files from the internet")
        print(Fore.WHITE + "imgoptf: enchances image quality")
        print(Fore.WHITE + "math: does math")
        print(Fore.WHITE + "python:Allows you to execute python file withing terminal")
        print(Fore.WHITE + "stoptask: stops a running process or application")

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

    elif cmd =="tasklist":
        output = os.popen('wmic process get description, processid').read()
        print(Fore.WHITE + output)

    elif cmd == "file_compare":
        try:
            x = input(Fore.BLUE + "First File:")
            y = input(Fore.BLUE + "Second File:")
            with open(x) as file1, open(y) as file2:
                file1_text = file1.readlines()
                file2_text = file2.readlines()
            for line in difflib.unified_diff(
                    file1_text, file2_text, fromfile=x,
                    tofile=y, lineterm=''):
                print(Fore.WHITE + line)
        except FileNotFoundError as e:
            print(Fore.RED + f"Error: {e.filename} not found")
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

    elif cmd == "file_tree":
        def generate_directory(
                tree, item, index, len_diritems, prefix, connector
        ):
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
                    generate_directory(
                        tree, item, index, len_diritems, prefix, connector
                    )
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
            print( Fore.RED + f"Error: {str(e)}")
        except Exception as e:
            print( Fore.RED + f"Error: {str(e)}")
    elif cmd == "serial_number":
        print(Fore.WHITE +"Serial number:"+ current_machine_id)

    elif cmd == "ren":
        try:
            new_address = input(Fore.BLUE + "Source address of the file:")
            new_dest = input(Fore.BLUE + "Destination of the file with the new name")
            os.rename(new_address, new_dest)  # renames and puts it in a new destination
            print(Fore.WHITE + "FILE SUCCESSFULLY RENAMED")
        except FileNotFoundError:
            print(Fore.RED + "Error: Could not find file")

    elif cmd == "cal":
        print(Fore.WHITE + calendar.month(yy,mm))

    elif cmd == "search":
        rootDir = input(Fore.BLUE + "Path of the file you want to search")
        fileToSearch = input("Name of the file")
        for relpath,dirs,files in os.walk(rootDir):  #loop for finding file
            if(fileToSearch in files):
                fullPath = os.path.join(rootDir,relpath,fileToSearch)
                print(Fore.WHITE + fullPath)
            else:
                print("                                ")
                print(Fore.RED + "Could not find file")
                break

    elif cmd == "clr":
        os.system('cls')

    elif cmd == "hangman":
        hangman = os.startfile("game.bat")

    elif cmd == "file_info":
        try:
            file_input = input(Fore.BLUE + "path of the file")
            file_size = os.path.getsize(file_input)
            file_extension = pathlib.Path(file_input).suffix
            print(Fore.WHITE + "File size:", file_size, "bytes")
            print(Fore.WHITE + "File type:", file_extension)
        except FileNotFoundError:
            print(Fore.RED + "Error: Could not find file")


    elif cmd == "dweb":
        try:
            url = input( Fore.BLUE + "Enter the URL of the file you want to download: ")
            filename = input(Fore.BLUE + "Enter the filename you want to save the file as: ")

            urllib.request.urlretrieve(url, filename)
            print("File Saved")
        except ValueError:
            print(Fore.RED + "Error: Invalid URL entered")
        except urllib.error.HTTPError as e:
            print(Fore.RED + f"Error: HTTP Error {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            print(Fore.RED + "Error: Failed to reach server")
            print(Fore.RED + f"Reason: {e.reason}")
        except Exception as e:
            print( Fore.RED + "Error:", e)

    elif cmd == "imgoptf":
        try:
            x = input(Fore.BLUE + "Path to file: ")

            # Converting to RGB mode
            im = Image.open(x)
            im = im.convert('RGB')

            # Compressing
            im.save("Image1.jpg", optimize=True, quality=90)

            # Sharpening
            im = Image.open(x)
            im = im.filter(ImageFilter.SHARPEN)

            # Saving
            im.save(x)

            print("Image processing completed successfully!")

        except Exception as e:
            print(Fore.RED + "Error:", e)


    elif cmd == "math":
        try:
            mathv = input(Fore.BLUE + "Enter math sum: ")
            result = eval(mathv)
            print(result)
        except NameError:
            print(Fore.RED + "Invalid input. Please enter a valid mathematical expression.")
        except ZeroDivisionError:
            print(Fore.RED + "Invalid input. Division by zero is not allowed.")
        except TypeError:
            print(Fore.RED +"Invalid input. Please enter a valid mathematical expression.")
        except SyntaxError:
            print(Fore.RED + "Incorrect Syntax")
        except Exception as e:
            print( Fore.RED + "Error:", e)

    elif cmd == "python":
        try:
            python_file_path = input(Fore.BLUE + "Path to python file: ")

            process = subprocess.Popen(["python", python_file_path], stdout=subprocess.PIPE)

            # Get the output and error streams of the subprocess
            output, error = process.communicate()

            # Check if an error occurred during execution
            if error:
                raise Exception(error.decode())

            # Print the output
            print(output.decode())

        except Exception as e:
            print(Fore.RED + "Error:", e)

    elif cmd == "stoptask":
        try:
            process_name = input(Fore.BLUE + "Enter process:")
            subprocess.run(['taskkill', '/F', '/IM', process_name], check=True)
            print(f"Successfully killed the process '{process_name}'.")
        except subprocess.CalledProcessError:
            print(Fore.RED + f"Failed to kill the process '{process_name}'.")



    else:
        print(f"command {cmd} not found")
