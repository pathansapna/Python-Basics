mystr = '10101'
def strToBinary(mystr):
    for x in mystr:
        if x not in '01': return "Error. String with non-binary characters"
    num = int(mystr, 2)
    return num
print ("binary: {} integer:{}".format(mystr, strToBinary(mystr)))
