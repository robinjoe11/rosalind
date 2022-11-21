import math

def RandomString(strRandomString, stringArray):
    strRandomString = strRandomString.upper()
    cg = len(strRandomString.replace('A', '').replace('T', ''))
    at = len(strRandomString.replace('C', '').replace('G', ''))
    inputArray = stringArray.split()
    outputArray = []
    for i in range(0, len(inputArray)):
        prob = cg * math.log10(float(inputArray[i]) / 2) + at * math.log10((1 - float(inputArray[i])) / 2)
        outputArray.append(round(prob, 3))
    return outputArray




result = ' '.join(map(str, RandomString('TTTACGTGTATAGAGTGATGGCCGGCGCCAGCTGAGGCTTGAGGACGTAGCCCAGTCGATGTAGAGGCTGGATGCCGTCGCAGCC', '0.095 0.168 0.182 0.275 0.300 0.353 0.414 0.482 0.575 0.596 0.697 0.717 0.818 0.862 0.911')))

print (result)