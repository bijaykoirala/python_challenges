mapping = {}
for i in range(26):
    if i < 24:
        mapping[chr(65+i)] = chr(67+i)
    else:
        mapping[chr(65 + i)] = chr(65 + i - 24)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".upper()
result = ""
for ch in text:
    if ch in mapping:
        result += mapping[ch]
    else:
        result += ch

print(result)

