import subprocess
import zipfile
import os
import sys

# Global variables
PATH_TO_SCRIPT = __file__
PATH_TO_PROJECT = os.path.dirname(PATH_TO_SCRIPT)
#PATH_TO_LIBS = os.path.join(PATH_TO_PROJECT, 'libs')
PATH_TO_LIBS = os.path.join(PATH_TO_PROJECT, 'libs_test')
PATH_TO_DROP_POINT = os.path.join(PATH_TO_PROJECT, 'drop_point')
PATH_TO_WISHLIST = os.path.join(PATH_TO_PROJECT, 'wishlist.txt')

LOCAL_OS = sys.platform
LOCAL_PYTHON_VERSION = subprocess.check_output(['python', '--version']).decode('utf-8').split(' ')[1].split('\r')[0]

# Functions to install libraries

def install_libs(libs):
    for lib in libs:
        subprocess.call(['pip', 'install', lib])


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

def add_to_wishlist(lib_name, lib_required_version=None):
    with open(PATH_TO_WISHLIST, 'a') as wishlist:
        wishlist.write(f'{LOCAL_OS}:{LOCAL_PYTHON_VERSION}:{lib_name}:{lib_required_version}')

def clear_whitelist():
    os.remove(PATH_TO_WISHLIST)
    open(PATH_TO_WISHLIST, 'w').close()
    

    

# Functions to handle user input



# Debug

#print(LOCAL_OS)
#add_to_wishlist('lib1')
#clear_whitelist()



# Main

