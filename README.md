# python-logparser

Creating a python logparser to parse access_log using regular expression.

This logparser will make it easy for analyzing the access_log. This will make the logline in dictionary format, which will be easier to analyse and divide according to our requirement.

While normally orinting a logline form an access_log will look like the following. 
```sh
logfile = "/root/jewel/python/access_log"

with open(logfile, "r") as fh:
    
    for logline in fh:
        
        print(logline)
        
        break
```
Output 

---
```sh
185.39.146.215 - - [06/Aug/2019:04:27:37 +0000] "GET / HTTP/1.1" 200 163 "-" "Pingdom.com_bot_version_1.4_(http://www.pingdom.com/)"
```

We are now going to change this output like the following form using a logparser. 
```sh
{'host': '185.39.146.215', 
'identity': '-',
'user': '-', 
'time': '06/Aug/2019:04:27:37 +0000', 
'request': 'GET / HTTP/1.1', 
'status': '200',
'size': '163', 
'referer': '-',
'agent': 'Pingdom.com_bot_version_1.4_(http://www.pingdom.com/)'}
```
The above info is more understandable and easy to handle, because it is dictiory type. 

We are using Regular expression or regex to do this. This is the same language which is used in rewrite rules of apache. For doing this we need to import the re module. 
---
---
Code
```sh
import re

def parser(line):
  
  p = '(?P<host>.+?)\s(?P<identory>.+?)\s(?P<user>.+?)\s\[(?P<time>.+?)\]\s\"(?P<requests>.+?)\"\s(?P<status>\d{3})\s(?P<size>.*?)\s\"(?P<referer>.*?)\"\s\"(?P<agent>.*?)\"'          
  result = re.match(p,line)
  return result.groupdict()
```
---
Calling the function
---

---
```sh
logFile = "/root/jewel/python/access_log"

with open(logFile,"r") as fh:
    
    for logLine in fh:
        
        parsedLine = parser(logLine)   
        
        print(parsedLine)
        break
```
We can create a module called logparser by saving the function in logparser.py
Then later we can import it in our other scripts. I ahve also added the logparser.py in this repo. 
Using that module will look like below.
```sh
import logparser

logfile = "/root/jewel/python/access_log"

with open(logfile,"r") as fh:
    
    for logline in fh:
                
        output = logparser.parser(logline)
        
        print(output)
        
        break
```

For other log analyzing using this logparser, please check my other repo >> [link](https://github.com/j4jewel/python-logfile-analysis)




