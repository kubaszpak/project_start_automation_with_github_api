import sys
import os
from github import Github

folder_name = sys.argv[1]

try:
    os.makedirs(folder_name, exist_ok=True)
    token = os.environ['GT']
    g = Github(login_or_token=token)
    u = g.get_user()
    repo = u.create_repo(name=folder_name, private=False,
                         gitignore_template='Python', license_template='mit')
except FileExistsError as e:
    print(e)
except KeyError as e:
    print('''Fistly you need to initialize a new env variable GT,
    and set it to your Github token''')
