author- Ashutosh Singh Parmar
github ID- parmAshu
email- ashutoshsingh291999@gmail.com
url- https://github.com/parmAshu/videoStream.git
start date- 12/April/2020 
target - separate thread to read frames from cameras (This increases speed significantly)

status-....................... 
system tested on- unbuntu 16 LTS, Raspbian, Ubuntu 18 LTS (windows and macos tests pending)

project layout-

videoStream/
|
|___project/
|         |
|         |___ openCV/ videoStreamCV.py
|         |
|         |___ picamera/ videoStreamPI.py
|
|
|___docs/
|      |
|      |___openCV/ cvStreamDoc.txt 
|      |
|      |___ picamera/ piStreamDoc.txt
|
|
|___examples/
|          |
|          |___streamexample.py
|
|
|___install/
|         |
|         |___linux/ install_dependencies.sh
|         |
|         |___Raspbian/ install_dependencies.sh
|
|___README.txt
|
|___HOW_TO_CONTRIBUTE.txt


IMPORTANT INFORMATION:

This project contains python3 modules for managing separate threads for reading frames from cameras. This technique significantly increases the
speed of main program as it does not have to wait for the frames to be read before starting to process them.

  PREPARING THE LINUX SYSTEMS:
    1. Having cloned the respository navigate into the install directory.
    2. Now navigate into one the linux subdirectory
    3. Here you will find a script named install_dependencies.sh
    4. provide executable rights to this script using the following command
       chmod +x install_dependencies.sh
    5. Now, execute the shell script using the following command
       ./install_dependencies.sh
    6. If the script show device offline message then, ensure a strong internet connection and rerun the script
    7. Once, the script has been executed successfully, the system is ready for the module usage.

    NOTE- if you are using a raspbian operating system then, it is highly recommended to perform the above steps with the shell script in 
          Raspbian directory.
 
 
  PREPARING THE WINDOWS SYSTEMS:
  --under development/testing--

  PREPARING THE MAC SYSTEMS:
  --under development/testing--

 
