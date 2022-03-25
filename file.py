import os
import datetime
import shutil

source = ("enter source: ")
destination = input("enter Destination: ")
source =source+'/'
destination=destination+'/'
list_of_files = os.listdir(source)

for file in list_of_files:
    shutil.copy((source+file),destination)
    print("file copied")
    