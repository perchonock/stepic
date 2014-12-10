
import requests
import re
with open('dataset_3378_3.txt', "r") as inf:
    url = inf.readline()
#    url = re.sub('https', 'http', url1)

print(url)
r = requests.get(url)
print(r)
folder = 'http://stepic.org/media/attachments/course67/3.6.3/'

while True:
    r = requests.get(folder + r.text)
    print(folder + r.text)
    print(r)
    if r.text.split()[0] == "We":
        break

print("finished")