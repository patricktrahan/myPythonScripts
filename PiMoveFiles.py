# Move files from Raspberry Pi to local folder then opens the folder to view the files

import os
import shutil
import subprocess
import sys

# security camera video files source folder
source = r'\\RaspberryPiName\\PiShareFolder'
# destination for video file to be moved
destination = r'C:\\Users\\UserName\\FileFolderLocation'

# collects all files from the source folder and moves to  the destination
for file in os.listdir(source):
	sourceFile = os.path.join(source, file)
	destinationFile = os.path.join(destination, file)
	shutil.move(sourceFile, destinationFile)

# opens the destination folder for viewing the moved files
subprocess.Popen('explorer "C:\\Users\\UserName\\FileFolderLocation"')
