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



class LRU:

    q = Queue.PriorityQueue()
    d ={}
    pp = pprint.PrettyPrinter(indent=4)
    indexes=[]
    pages=[]
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
            #    d[groupIndex] = []
            #    d[groupIndex].append(decimal)
            #    print d

                indexes.append(groupIndex)
        #        new = indexes[groupIndex]
                pages.append(decimal)
                zipz=zip(indexes,pages)
            #    print zipz
            except:
            #     pass
                # pages.append(decimal)

                 d[groupIndex] = []
            d[groupIndex].append(decimal)



        validBitP1 = [1]*55
        resBitP1 = [0]*55
        newItems=d['P1:']


        procNames='P1:'
        zippedP1 = zip(newItems, validBitP1, resBitP1)
        keyValue = groupIndex
        vals = d['P1:']

        x = [] #page numbers
        y =[] #validBit list
        ra =range(16) #resident bit list
        rb=range(16)
        n=[] #processID list
        p=[] #procID and page Number list
        frameTable=range(31)
        newX= []
        newP1=[]
        newP2 =[]
        newP3=[]
        newP4=[]
        newP5=[]
        newFrame= range(16)
        def lruLogic():
            for procNum, pageNum in zipz:
              # print zipz
               if (procNum, pageNum) in newX:

                #   indexed=[j[0] for j in zipFrame if j[1]==((procNum, pageNum))]
                # print newX.index((procNum,pageNum))
                indexed = newX.index((procNum,pageNum))
                newX.append(newX.pop(indexed))
                print ((procNum, pageNum), "Moved to end of list")
                # t = pT()
                # t.procTable1()

                # print indexed
                pTable1()
               if (procNum, pageNum) not in newX and len(newX)<16:

                   newX.append((procNum,pageNum))

                #    zipFrame = zip(newFrame, newX)
                   print ("Page Fault occured for :",(procNum, pageNum))
                   if(procNum=='P1:'):
                         newP1.append((pageNum))
                   if(procNum=='P2:'):
                         newP2.append((pageNum))
                   if(procNum=='P3:'):
                         newP3.append((pageNum))
                   if(procNum=='P4:'):
                         newP4.append((pageNum))
                   if(procNum=='P5:'):
                         newP5.append((pageNum))

               if (procNum, pageNum) not in newX and newX[15] != None:

                   newX.pop(0)
                   newX.append((procNum,pageNum))

                   print("Removing Victim, Page Fault occured for:",(procNum, pageNum))
                   if(procNum=='P1:' and pageNum not in newP1):
                       newP1.append((pageNum))
                   if(procNum=='P2:'and pageNum not in newP2):
                       newP2.append((pageNum))
                   if(procNum=='P3:'and pageNum not in newP3):
                       newP3.append((pageNum))
                   if(procNum=='P4:'and pageNum not in newP4):
                       newP4.append((pageNum))
                   if(procNum=='P5:'and pageNum not in newP5):
                       newP5.append((pageNum))
            zipFrame = zip(newFrame, newX)
        # for  pageNum, vBit, rBit in zip(newItems, validBitP1, resBitP1):
        #
        #     if pageNum in x:
        #         pass
        #     if pageNum not in x:
        #         x.append(pageNum)
        #         y.append( vBit)
        #         # r.append(1)
        #         n.append("p1:")
        #         z =  zip(n,x)
        #         p.append(z)
        #
        #         print (pageNum, "added to P1 page table")
        #     frm = map(str,x)

        def pTable1():
            ####process table p1
            pageTableP1 = [[],
            ['Page #', 'Frame#'],
            [('\n'.join(map(str,newP1))),

            ('\n'.join(map(str,([i for i,c in enumerate(zipFrame) if c[1][0]=='P1:'   ]))))]
            ]
            table = AsciiTable(pageTableP1)
            table.title='---P1 Page Table'
            print table.table
            # return None
        def pTable2():
            ####process table p2
            pageTableP2 = [[],
            ['Page #', 'Frame#'],
            [('\n'.join(map(str,newP2))),

            ('\n'.join(map(str,([i for i,c in enumerate(zipFrame) if c[1][0]=='P2:'   ]))))]
            ]
            table2 = AsciiTable(pageTableP2)
            table2.title='---P2 Page Table'
            print table2.table
        def pTable3():
            ####process table p3
            pageTableP3 = [[],
            ['Page #', 'Frame#'],
            [('\n'.join(map(str,newP3))),

            ('\n'.join(map(str,([i for i,c in enumerate(zipFrame) if c[1][0]=='P3:'   ]))))]
            ]
            table3 = AsciiTable(pageTableP3)
            table3.title='---P3 Page Table'
            print table3.table
        def pTable4():
            ####process table p4
            pageTableP4 = [[],
            ['Page #', 'Frame#'],
            [('\n'.join(map(str,newP4))),

            ('\n'.join(map(str,([i for i,c in enumerate(zipFrame) if c[1][0]=='P4:'   ]))))]
            ]
            table4 = AsciiTable(pageTableP4)
            table4.title='---4 Page Table'
            print table4.table

        def pTable5():
            ####process table p5
            pageTableP5 = [[],
            ['Page #', 'Frame#'],
            [('\n'.join(map(str,newP5))),

            ('\n'.join(map(str,([i for i,c in enumerate(zipFrame) if c[1][0]=='P5:'   ]))))]
            ]
            table5 = AsciiTable(pageTableP5)
            table5.title='---P5 Page Table'
            print table5.table
        def frameTable():
            frameTableP1 = [
            [],['Frame#', 'Process#', 'Page#'],
            [('\n'.join(map(str,range(16)))),('\n'.join(map(str,[j[1][0] for j in zipFrame]))),
            (('\n'.join(map(str,[l[1][1] for l in zipFrame]))))]
            ]
            table1 = AsciiTable(frameTableP1)
            table1.title='--------FRAME TABLE'
            print table1.table
    #    pp.pprint(d['P2:'])
        validBitP2 = [1]*len(d['P2:'])
        resBitP2 = [0]*len(d['P2:'])
        zippedP2 = zip(d['P2:'], validBitP2, resBitP2)


    # #    print zippedP2
    #
    # #    pp.pprint(d['P3:'])
    #     validBitP3 = [1]*len(d['P3:'])
    #     resBitP3 = [0]*len(d['P3:'])
    #     zippedP3 = zip(d['P3:'], validBitP3, resBitP3)
    # #    print zippedP3
    #
    # #    pp.pprint(d['P4:'])
    #     validBitP4 = [1]*len(d['P4:'])
    #     resBitP4 = [0]*len(d['P4:'])
    #     zippedP4 = zip(d['P4:'], validBitP4, resBitP4)
    # #    print zippedP4
    #
    # #    pp.pprint(d['P5:'])
    #     validBitP5 = [1]*len(d['P5:'])
    #     resBitP5 = [0]*len(d['P5:'])
    #     zippedP5 = zip(d['P5:'], validBitP5, resBitP5)
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
