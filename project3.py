from itertools import izip
from collections import defaultdict
import pprint
from collections import Counter
from itertools import chain
import struct
import Queue
from Queue import PriorityQueue
from time import gmtime, strftime
import time
from itertools import izip, imap
from terminaltables import AsciiTable


# class PCD(object):
#     def __init__(self, proc, priority):
# #        PriorityQueue.__init__(self)
#         self.proc = proc
#         #self.page = page
#         self.priority = 0
#         print 'process: \n', proc
#     #    print 'page: \n', page
#     #    print 'priority \n', priority
#         return
#     def __cmp__(self,other):
#         return cmp(self.priority, other.priority)
#

# sdef getVirtualMem(numFrames, lruAlgorithm, )

q = Queue.PriorityQueue()
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
        count = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        groupIndex = processID
        try:
            new = d[groupIndex]
        #    q.put( (new, count))


        except:

            d[groupIndex] = []
        d[groupIndex].append(decimal)


    pp.pprint(d)
    validBitP1 = [1]*55
    resBitP1 = [0]*55
    newItems=d['P1:']

    procOne=d['P1:']
    procTwo=d['P2:']
    procThree=d['P3:']
    procFour=d['P4:']
    procFive=d['P5:']

    procNames='P1:'
    zippedP1 = zip(newItems, validBitP1, resBitP1)
    keyValue = groupIndex
    vals = d['P1:']

    bigList =[]
    bigList.extend(procOne)
    bigList.extend(procTwo)
    bigList.extend(procThree)
    bigList.extend(procFour)
    bigList.extend(procFive)
    newBig = zip(groupIndex, bigList)
#    pp.pprint(d)
#    print newBig
    x = [] #page numbers
    y =[] #validBit list
    r =[] #resident bit list
    n=[] #processID list
    p=[] #procID and page Number list
    frameTable=range(16)

    for  pageNum, vBit, rBit in zip(newItems, validBitP1, resBitP1):

        if pageNum in x:
            pass
        if pageNum not in x:
            x.append(pageNum)
            y.append( vBit)
            r.append(1)
            n.append("p1:")
            z =  zip(n,x)
            p.append(z)

            print (pageNum, "added to P1 page table")
        frm = map(str,x)


#terminaltable print#
    pageTableP1 = [[],
    ['Page #', 'Frame#'],
    [('\n'.join(map(str,x))),
    ('\n'.join(map(str,(i for i,x in enumerate(frm)))))]
    ]
    table = AsciiTable(pageTableP1)

    table.title='---P1 Page Table'
    print table.table



    frameTableP1 = [
    [],['Frame#', 'Process#', 'Page#'],
    [('\n'.join(map(str,frameTable))),('\n'.join(map(str,n))), (('\n'.join(map(str,x)))) ]
    ]
    table1 = AsciiTable(frameTableP1)
    table1.title='--------FRAME TABLE'
    print table1.table
#    pp.pprint(d['P2:'])
    validBitP2 = [1]*len(d['P2:'])
    resBitP2 = [0]*len(d['P2:'])
    zippedP2 = zip(d['P2:'], validBitP2, resBitP2)


#    print zippedP2

#    pp.pprint(d['P3:'])
    validBitP3 = [1]*len(d['P3:'])
    resBitP3 = [0]*len(d['P3:'])
    zippedP3 = zip(d['P3:'], validBitP3, resBitP3)
#    print zippedP3

#    pp.pprint(d['P4:'])
    validBitP4 = [1]*len(d['P4:'])
    resBitP4 = [0]*len(d['P4:'])
    zippedP4 = zip(d['P4:'], validBitP4, resBitP4)
#    print zippedP4

#    pp.pprint(d['P5:'])
    validBitP5 = [1]*len(d['P5:'])
    resBitP5 = [0]*len(d['P5:'])
    zippedP5 = zip(d['P5:'], validBitP5, resBitP5)
#    print zippedP5




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
