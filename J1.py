import urllib.request
import json
counts = list()
url='http://py4e-data.dr-chuck.net/comments_555859.json'
data = urllib.request.urlopen(url).read()
try: js = json.loads(data)
except: js = None
comments = js['comments']
for comment in comments:
  counts.append(comment['count'])
print ('Count', len(comments))
print ('Sum', sum(counts))
