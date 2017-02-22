import argparse
import json
import sys
from subprocess import call
import urllib
import requests

"""
Usage:
  Used to pull images from omeka into the directory where script is called.
  Takes two inputs:
    - "omeka_id" which is the omeka id of the text
    - "output_file_name_head" which is the starting part of the output jpg, hopefully the TEI id e.g.,
         "HV_WA_1809_v3_"
      with the tail numbers and file extension to be filled in later.
"""

# add arguments
parser = argparse.ArgumentParser()
parser.add_argument("omeka_id")
parser.add_argument("output_file_name_head")
args = parser.parse_args()

#get json
URL         = "https://pennstreaty.haverford.edu/qi/api/files?item=" + args.omeka_id
r           = requests.get(URL)
json_list   = r.json()

# this is the number that we will subtract from the ids to get appropriate tail number
base_number = json_list[0]["id"] - 1 # this will make the first item 1, next 2 etc.

"""
Each item in json_list is a dictionary representative of a page in the text.
We are interested in the file_urls, and want the fullsize pictures
"""
for item in json_list:
  jpg_url = item["file_urls"]["fullsize"]
  num = item["id"] - base_number
  filename    = args.output_file_name_head
  if num<10:
    filename += ('00' + str(num) + '.jpg')
  elif num <100:
    filename += ('0'  + str(num) + '.jpg')
  else:
    filename += (str(num) + '.jpg')

  urllib.urlretrieve(jpg_url, filename)
