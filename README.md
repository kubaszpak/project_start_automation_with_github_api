# project_start_automation_with_github_api

Batch and python script used for automating the process of creating a git repository with the help of PyGitHub Api on Windows

## Setup

To set this up you will need to create a couple of environmental variables:

1. GT - github access token, you can create one of these in your github account settings, just make sure you check controlling repositories

2. PYTHONPATH - a full path to where your python modules are stored

3. GU - github username

4. Path - to this one you need to add '%PYTHONPATH%\create_git\'

## Usage

Now you're ready to use the script. In the command line navigate to your PYTHONPATH. Then:

        git clone https://github.com/kubaszpak/project_start_automation_with_github_api.git

Now you can use fully use it. Try it out with:

        create <new_repository_name>

This command you can run anywhere in your system. Just type it out and it will create a new repository in your account. And link it to the local one. It should create a README, add a MIT License and a python .gitignore. If you want to change the language just open the \_\_main\_\_ file and switch it in create_repo() function. The last thing it will do is opening Visual Studio Code if you have it set up correctly.
