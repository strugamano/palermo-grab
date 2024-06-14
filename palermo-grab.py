import sys
from urllib.request import urlretrieve

with open(sys.argv[1], 'r') as source: lines = source.readlines()

files, dir, i = [], "download/", 0

for url, name in zip(lines[::2], lines[1::2]): files.append({'url': url.rstrip(), 'name': name.rstrip()})

for file in files:
    i += 1
    urlretrieve(file['url'], dir + file['name'] + ".jpeg")
    print(f"{i}/{len(files)} done: {file['name']}")
