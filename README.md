# python_offline_lib_manager
This tool is designed as an installer/manager for python libraries, for off-network machines that can't use pip.

## Statement of Use
The tool is designed to be run from the command line, and will prompt the user for the name of the library they wish to install. The tool will then search the local directory for a matching library. It will verify that the library is available for the local python version, and if found, will install it. If the library is not found in the 'libs' dir, the tool will check if it was placed in the 'drop point' dir by the user. If the library is found in the drop point, it will be moved to the libs dir, and then installed. If the library is not found in the drop point, the tool will notify the user and ask if the missing lib should be added to the wishlist.

## Components
- **lib_manager.py** - The main script. This is the only file that needs to be run.
- **libs** - This directory is where the tool will look for libraries to install. The tool will search for a matching library in this directory, and if found, will install it.
- **drop_point** - This directory is where the tool will look for libraries that the user has placed there. If the tool finds a library in this directory, it will move it to the libs directory, and then install it.
- **wishlist.txt** - This file is where the tool will store libraries that the user has requested, but are not available in the libs directory. The tool will notify the user if a library is not found, and will ask if the library should be added to the wishlist. The user can then add the library to the wishlist. The wishlist will be used to automate lib downloads in the future.

## Use Case
- User sets up a new off-network machine, and wants to install a library.
- User runs the tool, and is prompted for the name of the library they wish to install.
- User enters the name of the library, and the tool searches the libs directory for a matching library.
- If the library is found, the tool will verify that the library is available for the local python version, and if found, will install it.
- If the library is not found in the libs dir, the tool will check if it was placed in the drop point dir by the user.
- If the library is found in the drop point, it will be moved to the libs dir, and then installed.
- If the library is not found in the drop point, the tool will notify the user and ask if the missing lib should be added to the wishlist.

## Future use of wishlist
- User copies the wishlist and sends it by email to an automated downloader.
- The downloader will download the libraries, archive them and send them back to the user.
- The user can then download the archive, analyze it to make sur it is safe, and then copy it to the drop point.
- The user can now run the tool and install the libraries.


## To Do
- [ ] Add version checking
- [x] Add wishlist functionality
- [x] Add drop point functionality
- [ ] Add optionnal GUI
- [ ] Add basic python installer/update