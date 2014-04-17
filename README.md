Dropbox-Folder-Size
===================

A small Python script that generates a .txt file of the sizes of your Dropbox folders. Perfect for checking the sizes of folders that you have selectively unsync-ed.

# Script Requirements
===================

1. Python SDK
Installation instructions [here](https://www.dropbox.com/developers/core/sdks/python).

2. Dropbox Access Token
Still new to Dropbox development, so I'm not sure what the proper way of getting an access token is, but the way I did it was by: 

1. Visiting [Dropbox's Developer site and going to App Console](https://www.dropbox.com/developers/apps).
2. Create a Dropbox API app with "Files and Datastores", "No", "All file types" options.
3. Get the app key, visit this [website](https://dbxoauth2.site44.com/) and it will generate an access token for you.

# Usage Instructions

Input your access token into the script.

The script accepts 2 variables:

1. Denominator (non-negative integer). 0 for bytes, 1 for KB, 2 for MB, 3 for GB, etc.

2. Levels (non-negative integer). Tells the script how far down the directory tree you want to look. E.g. if set to 1, the script will output the sizes of all your folders in the main Dropbox directory.

# Known Bugs

1. Dropbox still thinks .pages documents are folders. I might or might not get around to fixing this.

# Possible Features

1. Make this script a full-fledged app, with browser redirection for OAuth authentication and stuff.
2. Add support to run script in sub-folders.
3. Add a switch to un-ignore files that appear above the set level.