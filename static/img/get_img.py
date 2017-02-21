import argparse
import json
import sys
from subprocess import call
import urllib
parser = argparse.ArgumentParser()
parser.add_argument("json_file")
args = parser.parse_args()
with open(args.json_file,"r") as f:
  json_string = f.read()
  json_list   = json.loads(json_string)
  url         = json_list["file_urls"]["fullsize"]
  num = int(args.json_file) - 4440 #this makes it non-flexible
  filename = 'HV__JS1798_1800_'
  if num<10:
     filename += ('00' + str(num) + '.jpg')
  else:
     filename += ('0'  + str(num) + '.jpg')
  urllib.urlretrieve(url,filename)

  # sys.stdout.write(url)

  # call('wget ' + url, shell=True)
  '''
  try:
    print url
    sys.stdout.flush()
  except IOError as e:
    if e.strerror.lower() == 'broken pipe':
      exit(0)
    raise
  '''
