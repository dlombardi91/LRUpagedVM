from itertools import izip
from collections import defaultdict
import pprint
from collections import Counter
from itertools import chain



d ={}
pp = pprint.PrettyPrinter(indent=4)
with open("input3a.data") as f:
    for line in f:
        info = line.split()
        processID = info[0]
        pageNumber = info[1]
        int(pageNumber,2)
        binary = pageNumber
        decimal = 0
        #i=0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        groupIndex = processID
        try:
            blah = d[groupIndex]
        except:
            d[groupIndex] = []
        d[groupIndex].append(decimal)


    pp.pprint(d)



    for key, values in sorted(d.items()):

        print ('{} {}'.format(key+'Has a total of', len(values))+' memory references')
    f.close()

de = defaultdict(set)
with open('input3a.data') as tf:
    for line in tf:
        if line.strip():

            info = line.split()
            processID = info[0]
            pageNumber = info[1]
            int(pageNumber,2)
            binary = pageNumber
            decimal = 0
            for digit in binary:
                    decimal = decimal*2 + int(digit)
            de[processID].add(decimal)
for k,v in sorted(de.iteritems()):
    print('{} {}'.format('Process '+k+' total size in pages',len(v)))
