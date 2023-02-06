#!/usr/bin/env python3
import os
import argparse

# Parsing the argument
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", dest="filename", help="Name of the folder and file to be created")
args = parser.parse_args()

# Creating the folder
folder_name = args.filename
os.makedirs(folder_name)

# Creating the file inside the folder
file_path = os.path.join(folder_name, f"{args.filename}.py")
with open(file_path, "w") as file:
    file.write("#!/usr/bin/env python3\n")
    file.write("\n")
    file.write("# Author: Your Name <your.email@example.com>\n")
    file.write("# Project Name: " + args.filename + "\n")
    file.write("\n")
    file.write("'''\n")
    file.write("Copyright (c) 2023 Your Name\n")
    file.write("\n")
    file.write("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n")
    file.write("\n")
    file.write("The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n")
    file.write("\n")
    file.write("THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n")
    file.write("'''\n")


# Changing the file permissions to make it executable
os.chmod(file_path, 0o755)
