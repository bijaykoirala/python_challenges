# question url : http://www.pythonchallenge.com/pc/def/equality.html

def main():
    data = open("proof.txt").read()

    for i in range(4, len(data) - 4):
        a,b,c,d = data[i-4], data[i-3], data[i-2], data[i-1]
        letter  = data[i]
        h,g,f,e = data[i+4], data[i+3], data[i+2], data[i+1]
        first_middle_last_lower = a.islower() and letter.islower() and h.islower()
        prev_upper = b.isupper() and c.isupper() and d.isupper()
        later_upper =  e.isupper() and f.isupper() and g.isupper()
        
        if first_middle_last_lower and prev_upper and later_upper:
            print(letter, end="")

main()
# next url : http://www.pythonchallenge.com/pc/def/linkedlist.php
