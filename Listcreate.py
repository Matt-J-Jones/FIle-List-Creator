import os
import xlwt
def cleartxt():
    f=open("filelist.txt", "w")
    f.write("")
def cleanup(filename_todelete):
    with open("filelist.txt", "r") as f:
        lines = f.readlines()
    with open("filelist.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != filename_todelete:
                f.write(line)
def generatelist():
    for root, dirs, files in os.walk("."):
        for filename in files:
            x_ext=filename
            x=x_ext.replace(".pdf","")
            f=open("filelist.txt", "a")
            f.write(x)
            f.write("\n")
            f.close()
cleartxt()
generatelist()
cleanup("Listcreate.py")
cleanup("filelist.txt")
cleanup("Thumbs.db")