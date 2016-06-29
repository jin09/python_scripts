import os

def rename_file():
    #get the list of all the file names from the target folder
    list_name = os.listdir("C:\Users\gautam\Desktop\prank")
    print(list_name)
    os.chdir("C:\Users\gautam\Desktop\prank")
    cd = os.getcwd()
    print(cd)
    #rename the file names to remove the numerics
    for file_name in list_name:
        os.rename(file_name,file_name.translate(None,"1234567890"))


rename_file()
