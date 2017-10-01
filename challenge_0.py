import math

number = math.pow(2, 38)
url = str.format("http://www.pythonchallenge.com/pc/def/{0}.html", int(number))
print("Navigate to => " + url)
