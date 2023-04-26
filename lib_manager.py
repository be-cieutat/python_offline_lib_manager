import subprocess
import zipfile
import os

# Global variables
PATH_TO_SCRIPT = __file__
PATH_TO_PROJECT = os.path.dirname(PATH_TO_SCRIPT)
PATH_TO_LIBS = os.path.join(PATH_TO_PROJECT, 'libs')
PATH_TO_DROP_POINT = os.path.join(PATH_TO_PROJECT, 'drop_point')
PATH_TO_WISHLIST = os.path.join(PATH_TO_PROJECT, 'wishlist.txt')

LOCAL_PYTHON_VERSION = subprocess.check_output(['python', '--version']).decode('utf-8').split(' ')[1].replace('\n','')

# Functions to install libraries


# Functions to sort libraries from drop_point into libs

def unzip_archive(archive):
    with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall(PATH_TO_DROP_POINT)
    

def sort_libs():
    for lib in os.listdir(PATH_TO_DROP_POINT):
        if lib.endswith('.zip'):
            unzip_archive(lib)
            os.remove(os.path.join(PATH_TO_DROP_POINT, lib))
# TO COMPLETE


# Functions to manage wishlist.txt

# Wishlist entry format: <os>:<python_version>:<lib_name>:<lib_required_version>\n
# <lib_required_version> is optional, useful if specific lib version is a dependency of another lib.




# Functions to handle user input


# Main

