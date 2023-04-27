# Imports

import subprocess
import zipfile
import os
import sys
import shutil


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
        subprocess.check_call([sys.executable,'-m','pip','install',PATH_TO_LIBS])
        # TO COMPLETE
        

# Functions to sort libraries from drop_point into libs

def unzip_archives(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if file.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            os.remove(file_path)
    

def move_libs(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if file_path.endswith('.whl'):
            shutil.move(file_path, PATH_TO_LIBS)
        if os.path.isdir(file_path):
            for subfile in os.listdir(file_path):
                subfile_path = os.path.join(file_path, subfile)
                shutil.move(subfile_path, PATH_TO_LIBS)
            os.rmdir(file_path)
        
            
def sort_libs():
    pass

def manage_drop_point():
    unzip_archives(PATH_TO_DROP_POINT)
    move_libs(PATH_TO_DROP_POINT)
        
        
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
#add_to_wishlist('lib1') #OK
#clear_whitelist() #OK
#unzip_archive(PATH_TO_DROP_POINT+'/tt.zip') #OK
manage_drop_point() #OK
#sort_libs() #OK



# Main

