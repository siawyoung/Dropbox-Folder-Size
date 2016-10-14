import dropbox

client = dropbox.client.DropboxClient('<INSERT ACCESS TOKEN>')

# choose 0 to express values in bytes, 1 in KB, 2 in MB, 3 in GB.
denomination = 2

# choose how many levels you want to segregate by
# e.g. if levels is 1, will return folder sizes of folders in Dropbox root
# If you just want to know overall usage of account (i.e. levels = 0), we will run a separate query for it
levels = 2

output = open('dropbox_folder_sizes.txt', 'w')

if (levels == 0):
    quota_info = client.account_info()['quota_info']
    usage = quota_info['shared'] / (1024.0 ** denomination)
    quota = quota_info['quota'] / (1024.0 ** denomination)

    output.write('You are currently using ' + str(usage) + ' out of ' + str(quota) + ' of space on Dropbox.')
    output.close()
    quit()

sizes = {}
foldersizes = {}
cursor = None

while cursor is None or result['has_more']:
    result = client.delta(cursor)
    for path, metadata in result['entries']:
        sizes[path] = metadata['bytes'] if metadata else 0
    cursor = result['cursor']

for path, size in sizes.items():

    segments = path.split('/')

    if (len(segments) > levels + 1):
        folder = '/'.join(segments[0:levels+1])
    else:
        folder = '/'.join(segments[0:len(segments)-1])
    try:
        foldersizes[folder] += size
    except KeyError:
        foldersizes[folder] = size

if (denomination != 0):
    for path,size in foldersizes.items():
        if size:
            foldersizes[path] = size / (1024.0 ** denomination)
        else:
            del foldersizes[path]

output.write('Below is a list of your largest Dropbox folders, ordered from largest to smallest. You chose a drill level of 2. Sizes are expressed as "%d", where 0 is in bytes, 1 is in KB, 2 is in MB, and 3 is in GB. \n' % denomination)

for folder in reversed(sorted(foldersizes.keys(), key=lambda x: foldersizes[x])):
    output.write('%s: %f' % (folder.encode('utf-8'), foldersizes[folder]) + '\n')

print "File dropbox_folder_sizes.txt successfully created in the same directory as this script!"

output.close()
quit()
