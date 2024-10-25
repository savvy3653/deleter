
import os
from colorama import Fore, Back, Style


path = input('Enter the path: ')
extension = input('Enter the extension: ')
kb = int(input('Enter the size (in kilobytes): '))

byte = kb * 1000
for adress, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(adress, file)
        file_size = os.path.getsize(full_path)
        if file_size > byte and full_path.endswith(extension):
            os.remove(full_path)
            print(Fore.GREEN + f'File {full_path} has been succesfully deleted', Style.RESET_ALL)
input('\nPress Enter to escape...')
