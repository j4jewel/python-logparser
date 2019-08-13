#!/usr/bin/env  python3

import re

def parser(line):

  p = '(?P<host>.+?)\s(?P<identory>.+?)\s(?P<user>.+?)\s\[(?P<time>.+?)\]\s\"(?P<requests>.+?)\"\s(?P<status>\d{3})\s(?P<size>.*?)\s\"(?P<referer>.*?)\"\s\"(?P<agent>.*?)\"'
  result = re.match(p,line)
  return result.groupdict()
