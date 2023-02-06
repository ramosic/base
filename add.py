#!/usr/bin/env python3
import argparse
import os

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(f"{folder_name} already exists")

def create_readme(project_folder):
    with open(f"{project_folder}/README.md", "w") as file:
        file.write("# Project Name\n")
        file.write("Project description goes here\n")

def create_python_file(folder_name, filename):
    with open(f"{folder_name}/{filename}.py", "w") as file:
        file.write("#!/usr/bin/env python3\n")
        file.write("# Author: Christer Karlsen\n")
        file.write("# Email: chris@ramosicked.com\n")
        file.write(f"# Project: {filename}\n")
        file.write("# Copyright (c) 2023, Christer Karlsen\n")
        file.write("# License: MIT License\n")
        file.write("#\n")
        file.write("\"\"\"\n")
        file.write("Example script\n")
        file.write("\"\"\"\n")
    os.chmod(f"{folder_name}/{filename}.py", 0o755)

def create_github_repo(folder_name, repo_name):
    os.chdir(folder_name)
    os.system(f"git init")
    os.system(f"echo '# {repo_name}' > README.md")
    os.system(f"git add .")
    os.system(f"git commit -m 'Initial commit from add.py'")
    os.system(f"git remote add origin git@github.com:ramosic/{repo_name}.git")
    os.system(f"git push -u origin master")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Python project with a README and a Python file")
    parser.add_argument("-f", "--filename", required=True, help="Name of the project folder and the Python file")
    args = parser.parse_args()

    base_folder = os.path.dirname(os.path.abspath(__file__))
    folder_name = args.filename
    dev_folder = os.path.join(base_folder, "dev")
    prod_folder = os.path.join(base_folder, "prod")

    if not os.path.exists(dev_folder):
        os.mkdir(dev_folder)

    if not os.path.exists(prod_folder):
        os.mkdir(prod_folder)

    folder_path = os.path.join(dev_folder, folder_name)
    create_folder(folder_path)
    create_readme(folder_path)
    create_python_file(folder_path, args.filename)
    create_github_repo(folder_path, args.filename)
