import os
from git import Repo

bubblePath = os.getcwd() + '/bubbles'

bubblePrivatePath = os.getcwd() + '/bubbles/bubbles_private'

print bubblePath
print bubblePrivatePath


bubble_url = 'https://github.com/fxrhxn/testing-raspberrypi'
bubble_private_url = 'https://github.com/fxrhxn/testing-raspberrypi'

repo_dir = 'Random_S'

Repo.clone_from(bubble_url, bubblePath)
Repo.clone_from(bubble_private_url, bubblePrivatePath)
