# Automating file management
# Intsalling necessary libraries
# to get started, you will need to install two libraries: os & shutil
# Writing the automation script

import os
import shutil

source_folder = 'path/folder'
destination_folder = 'path/destination/folder'

for filename in os.listdir(source_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        source = os.path.join(source_folder, filename)
    destination = os.path.join(destination_folder, filename)
    shutil.move(source, destination)