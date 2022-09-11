import os
import fade
from colorama import Fore

# system check
if os.name == "nt":
    os.system("cls") # windows
else:
    os.system("clear")  # other

# banner #

banner = """
    ____                                   __     __
   / __ \__  ______  _________ _____  ____/ /__  / /
  / /_/ / / / / __ \/ ___/ __ `/ __ \/ __  / _ \/ / 
 / _, _/ /_/ / / / / /__/ /_/ / / / / /_/ /  __/ /  
/_/ |_|\__,_/_/ /_/\___/\__,_/_/ /_/\__,_/\___/_/   
                                                    

github.com/FozuX
"""
faded_banner = fade.purplepink(banner)
print(faded_banner)


# encrypt #

def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key", "wb") as key_out:
        key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)

# decrypt #

def decrypt(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open("decrypt_" + filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

# options #

options = f"""{Fore.LIGHTBLUE_EX}
[1] Encrypt
[2] Decrypt

[99] Exit 
"""
print(options)

# encrypt option #

option = int(input(f"{Fore.LIGHTBLUE_EX}╭── {Fore.WHITE}[{Fore.RED}Runcandel💀home{Fore.WHITE}]\n{Fore.LIGHTBLUE_EX}╰──────# {Fore.RESET}"))

if option == 1:
    file = input("|-~> File: ")
    encrypt(filename=file)
    print(filename)("Successfully encrypted!")

# decrypted options #

elif option == 2:
    file = input("|-~> File: ")
    key = input("|-~> Key: ")
    decrypt(filename=file, key=key)
    print("Successfully decrypted!")

# ================================================= #

elif option == 99:
    exit(-1)
        
