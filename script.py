import os
from git import Repo
import getpass


## Paths where the bubble directories should be saved.
bubblePath = os.getcwd() + '/bubbles'
bubblePrivatePath = os.getcwd() + '/bubbles/bubbles_private'

## Prompt User for username / password.
username = raw_input('Github Username:')
password = getpass.getpass('Github Password:')


## Authentication String.
auth = 'https://' + username + ':' + password

## Both bubble urls.
bubble_url = auth + '@github.com/bubblegroup/bubble'
bubble_private_url = auth + '@github.com/jphaas/bubble_private'



## Create the repos.
clonedRepo = Repo.clone_from(bubble_url, bubblePath)
clonedRepo2 = Repo.clone_from(bubble_private_url, bubblePrivatePath)

print clonedRepo
