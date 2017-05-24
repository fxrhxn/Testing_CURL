import os
from git import Repo

## Paths where the bubble directories should be saved.
bubblePath = os.getcwd() + '/bubbles'
bubblePrivatePath = os.getcwd() + '/bubbles/bubbles_private'

## Both bubble urls.
bubble_url = 'https://github.com/bubblegroup/bubble'
bubble_private_url = 'https://github.com/jphaas/bubble_private'

## Create the repos.
Repo.clone_from(bubble_url, bubblePath)
Repo.clone_from(bubble_private_url, bubblePrivatePath)
