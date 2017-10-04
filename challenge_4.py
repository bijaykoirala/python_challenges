import urllib.request

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
content = urllib.request.urlopen(baseurl).read()
newurl = baseurl + "?nothing=" + "12345"
okay = False
currentNumber = 0

# first following next nothing thing numbers
while (not(okay)):
    try:
        content = urllib.request.urlopen(newurl).read().decode('utf-8')
        newnumber = content.split("and the next nothing is ")[1]
        currentNumber = (int)(newnumber)
        newurl = baseurl + "?nothing=" + str(newnumber).strip()
        print(newurl)
    except IndexError: 
        okay = True

# it breaks the pattern at some point
# break at divide by 2 and keep going

okay = False
newurl = baseurl +"?nothing=" + str(currentNumber/2)
while (not(okay)):
    try:
        content = urllib.request.urlopen(newurl).read().decode('utf-8')
        newnumber = content.split("and the next nothing is ")[1]
        currentNumber = (int)(newnumber)
        newurl = baseurl + "?nothing=" + str(newnumber).strip()
        print(newurl)
    except IndexError:
        okay = True
        print(content)

# final url = "peak.html)
