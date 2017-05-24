import os
print os.getcwd()
from git import Repo

git_url = 'https://github.com/fxrhxn/testing-raspberrypi'

repo_dir = 'Random_S'
Repo.clone_from(git_url, "TestingMore")
