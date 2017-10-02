# question url : http://www.pythonchallenge.com/pc/def/equality.html

def main():
    data = open("proof.txt").read()

    for i in range(4, len(data) - 4):
        a,b,c,d = data[i-4], data[i-3], data[i-2], data[i-1]
        letter  = data[i]
        h,g,f,e = data[i+4], data[i+3], data[i+2], data[i+1]
        
        if a.islower() and b.isupper() and c.isupper() and d.isupper() and letter.islower() and e.isupper() and f.isupper() and g.isupper() and h.islower():
            print(letter, end="")

main()
# next url : http://www.pythonchallenge.com/pc/def/linkedlist.php
