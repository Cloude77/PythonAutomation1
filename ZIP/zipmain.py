from zipfile import ZipFile
from pathlib import Path
# 1

# create dir relative path

# Path('my-files').mkdir()
#
# with open("my-files/first.txt", 'w') as my_file:
#     my_file.write("This is first file")
#
# with open("my-files/second.txt", 'w') as my_file:
#     my_file.write("This is second file ")



# read my-files.zip
# 3

with ZipFile('my-files.zip') as my_zip_file:
    my_zip_file.extractall('my-files-unzipped') # create dir for archive from my-files.zip
    print(my_zip_file.infolist()) # list from 2 elements
    print(my_zip_file.filename) # title

# create archive from my-files
# 2
with ZipFile('my-files.zip', mode='w') as my_zip_file: # open file and write
   # print(my_zip_file)
    for file in Path('my-files').iterdir(): # iterate over all files
        print(file)
        my_zip_file.write(file)  # add my-files\first.txt my-files\second.txt in archie



