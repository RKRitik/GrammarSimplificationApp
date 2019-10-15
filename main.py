T = ['a','b']
V = ['A','B']
start_symbol = 'S'
epsilon_symbol = 'e'
S = []
valid = True
L = [] #stores all the LHS of the production rules
R = [] #rhs of productions
#string = ""
#temp = ""
start = 0

global_ = []
#------------------------------------------------------------------------------------
T = input('Enter the terminals ').split() # eg a b c do not put e as a terminal
V = input('Enter the non-terminals ').split() # eg A B
start_symbol = input('Enter the Start Symbol ')
epsilon_symbol = input('Enter the Epsilon Symbol ')

#------------------------------------------------------------------------------------
V.append(start_symbol)
T.append(epsilon_symbol)
# check(T,V)
p = ' '
#------------------------------------------------------------------------------------
def printFinal():
    for l,r in zip(L,R):
        r1 =""
        for k in r:
            r1+=str(k)
            r1+='|'
        r1 = r1[:-1]
        print(l,'->','',r1)
#------------------------------------------------------------------------------------
##################checking if the grammar is invalid
def checkInvalid():
    flag = False
    for r in R:
        for t in r:
            if t in T:
                flag = True

    return flag
#------------------------------------------------------------------------------------
#####################entering and checking the productions#######################################
def checkProduction(p):
     # print(p)
     if len(p)<1:
         return False
     for i in range(len(p)):
             if p[i] == '-':
                 l = str(p[:i])
                 r = p[i + 2:]
                 # print('l = ', l, 'V = ', V)
                 # print(' not l in V = ',not l in V)
                 if not l in V:                     # checking LHS
                     print(l, ' is not a valid non terminal \n')
                     return False
                 # print('r = ', r)
                 for j in range(len(r)): # checking RHS
                    temp = T[:]
                    temp.extend(V)
                    if not r[j] in temp :
                        print(r[j], ' is not a valid input \n')
                        return False
                    L.append(l)
                    R.append(r)
                    return True
# ------------------------------------------------------------------------------------
#####################converting RHS to nodes#######################################
def splitNodes():
    for i in range(len(R)):
        i_ = R[i].split('|')
        R[i]=i_
#------------------------------------------------------------------------------------
#####################produxctions simplification #######################################
def checkEpsilon():#check if e is in any of non starting symbols
    change = False
    for i in range(len(L)):
        #print('i = ',i)
        if not L[i]==start_symbol:
        #    print('R[i] = ',R[i])
            if epsilon_symbol in R[i]: #checking if RHS contains epsilon
       #         print('production : ',L[i],"-> ",R[i])
        #        print('epsilon found for L = ',L[i])
                change = True
                symbol = L[i]
                #substituting for e in current  non-terminal
                for j in  range(len(L)): #replacing this non terminal in other production

                    len_ = len(R[j])

                    #flag = False
                    for k in range(len_ - 1, -1,-1):  # traversing through each node in RHS to find the non terminal uses

                        global_.clear()
                        #print('k = ',k)
                        n = (R[j][k])
              #          print(R[j][k])
                        n = list(n)
                        #print('list(n) =', n)
                        temp = n
                        # print('z = ', z , ' i = ', i , 'n = ', n , ' L = ',L)
               #         print('symbol = ',symbol," temp = ",temp)
                        if symbol in temp:
                            if(len(temp)>1):
                #            print('symbol present in node index ', k)
                 #           print('R[j][k] = ',R[j][k])
                                fun(symbol,R[j][k])#recurcive function to find all combinations after substituting the symbol
                  #          print('out of fun function ')

                                R[j].extend(global_)
                                global_.clear()
                            else:
                                R[j].extend(epsilon_symbol)
                        #n = temp  # restoring

                    #if  flag and L[j]==start_symbol and not epsilon_symbol in R[j]:
                    #    R[j].append(epsilon_symbol)
                   # if epsilon_symbol in R[j] and not L[j] == start_symbol:
                    #    R[j].remove(epsilon_symbol)

    for i in range(len(L)):
         if not L[i]== start_symbol:
      #       print('L = ',L[i])
             len_ = len(R[i])
             for k in range(len_ - 1, -1,-1):
                # print('R[')
                 if R[i][k] == epsilon_symbol:
                     R[i].remove(epsilon_symbol)
    # print('new Productions : ')
    # for i in range(len(L)):
    #     print(L[i],'->' , R[i])


    removed = []
    for i in range(len(L)-1,-1,-1):
        if len(R[i])==0:

            removed.append(L[i])
            del R[i]
            del L[i]

    for i in range(len(L)):
        len_ = len(R[i])
        for j in range(len_ - 1, -1, -1):
            liss = list(R[i][j])

            for r in removed:
                if r in liss:
                    R[i].remove(R[i][j])
    #for l in R:
    # len_  = len(L)
    # for i in range(len_ - 1, -1,-1):
    #     if len(R[i])==0:
    #         symbol = L[i]
    #         for j in range(len(L)):
    #             len__ = len(R[j])
    #             for k in range(len__ - 1, -1, -1):
    #                 if symbol in list(R[j][k]):
    #                     R[j].remove(R[j][k])
    #         R.remove(R[i])
    #         V.remove(L[i])
    # for v in V:
    #     if not v in L and not v==start_symbol:
    #        for j in range(len(L)):
    #             len__ = len(R[j])
    #             for k in range(len__ - 1, -1, -1):
    #                 if v in list(R[j][k]):
    #                     R[j].remove(R[j][k])
    return change


def getSeq(string_,temp,start,symbol):
    #print('inside get seq function')
    #print('string = ',string)
    h = len(string_)
    #print('h = ',h)
    for i in range(start,h):
        #print('string[i] = ',string[i])
        if string_[i]==symbol :
            getSeq(string_,temp,i+1,symbol)
        temp+=string_[i]
    if temp!=string_ :
       # print('appendind ',temp, " in global_")
        global_.append(temp)
    return
def fun(symbol,temp__):
        #print('inside fun function')
        start = 0
        string_ = temp__
        #print("global = ",global_)
        #print('string = ',string)
        temp =""

        getSeq(string_,temp,start,symbol)
        # print('fun called , temp = ',temp)
        # if temp.count(symbol) > 0 :
        #     l = len(temp)
        #     for num in range(l - 1, -1,-1):
        #         if temp[num] == symbol:
        #             temp1 = temp
        #             del temp1[num]
        #             print('extended temp1 = ',temp1 )
        #             R[j].extend(temp1)
        #             fun(symbol,temp1,j,i,n)

        # while n.count(L[i]) > 0:
        #     flag = True
        #     print(n)
        #     n = list(n)
        #     n.remove(L[i])  # refactor
        #     n = list(n)
        #     print('n before  = ', n)
        #     # print(''.join(n)) #refactor this
        #     print('n after joining = ', n)
        #     if not n in R[j]:
        #         R[j].append(''.join(n))
list_units = []

def checkUnit():

    list_all = []

    change = False
    # #int_ = 0
    # #lis = []
    # le = len(L)
    # for i in range(le-1,-1,-1):
    #     values = []
    #     if len(R[i])>1:
    #         l = len(R[i])
    #         for j in range(l-1,-1,-1):
    #             lis = []
    #             print('R[i][j] = ',R[i][j])
    #
    #             if  R[i][j] in V: #finding the unit production
    #                print('remove ',R[i][j])
    #                change= True
    #                val = R[i][j]
    #                list_all.append(val)
    #                print('removing unit production',val)
    #             #   R[i].remove(val) #removing the unit production from production rules
    #                #in_ = L.index(val)
    #                values.extend(fun_(list_all))
    #                list_all.clear()
    #
    #
    #         R[i].extend(values)
    #         list_all.clear()
    #         values.clear()
    for i in range(len(L)-1,-1,-1):
        val = []
        for j in range(len(R[i])):
            if R[i][j] in V:

                in_ = L.index(R[i][j])
                for s in R[in_]:
                            if not s in V:
                                val.append(s)

            R[i].extend(val)


    for i in range(len(L)-1,-1,-1):
            temp = []
            for v in R[i]:
                if not v in V and not v in temp:
                    temp.append(v)

            R[i] = temp
            # if len(temp)==0:
            #     L.remove(L[i])
    lenn = len(L)
    for i in range(lenn-1,-1,-1):

            if len(R[i])==0:
                R.remove(R[i])
    return change
def fun_(list_all):
    check = 1
    for i in range(check):
        for i in range(len(R)):
            if L[i] in list_all:
               # print('copying the productions in ',L[i])
                for node in R[i]:
                    if node in V and (not node in list_all) :
                        list_all.append(node)
                        check+=1
    #print('list_all = ',list_all)
    values = []
    #printFinal()
    for k in range(len(R)):# traversing through production rules
        if L[k] in list_all :#checking if the lhs 's values needs to be substituted
            for l in range(len(R[k])-1,-1,-1):
                if not R[k][l] in V:
                    values.append(R[k][l])
                    #R[k].remove(R[k][l])
    #print('values = ',values)
    return values
    # list1 = []
    # for node in R[in_]:
    #     print('node = ',node)
    #     if len(node) > 1 or node ==epsilon_symbol:
    #         lis.append(node)
    #     else:
    #         if node in V:
    #             in_ = L.index(node)
    #             lis = fun_(in_,node,lis)
        # checking if the rhs is a terminal and it is  not same symbol , cosidering  epsilon production hav been removed
        # R[i].extend(node)
        #if node == epsilon_symbol and L[i] == start_symbol:  # allowing epsilon to replced only in start symbol
        #    list_units.append(node)

        #else:
         #   if node in V and node != val:
          #      list_units.append(join(node))

           # else:
            #    if node in T:
             #       list_units.append(join(node))


def checkUseLess():

    change = False
    useful = []

    for i in range(len(L)):
        for j in range(len(R[i])):
            newL = list(R[i][j])
            flag = True
            for l in newL:
                if l in V:
                    flag = False
            if flag and not L[i] in useful:
                useful.append(L[i])
    #print('usefull : ',useful)
    # useful = []
    # # print('R = ', R)
    # for i in range(len(L)):
    #     for node in R[i]:
    #         newList = list(node)
    #         print('newlist = ',newList)
    #         for n in newList:
    #             if  n in V and not n==start_symbol and not n in useful:
    #                 useful.append(L[i])
    # #now check if any node in RHS is made of only one of these useful symbols
    for  i in range(len(R)):
          for node in R[i]:
              if  node in useful:
                  useful.append(L[i])
    useLess = list(set(L)-set(useful))
     #removing the nodes the the productions containing useless non terminals
    # # print('R = ', R)
   # print(useLess)

    for u in useLess:
         for i in range(len(R)-1,-1,-1):
         #    print('i = ',i)
             for j in range(len(R[i])-1,-1,-1):
            #     print('j = ', j)
                 # print('R = ',R)
                 # print('R[i][j] = ',R[i][j])
                 node = R[i][j]

                 if u in R[i][j]:
                     R[i].remove(R[i][j])   #check this .....


    return change
def checkUnReachable():
    NotReached = list(set(V)-set(start_symbol))
    change = False
    for i in range(len(L)):
        if L[i]==start_symbol :
            for j in range(len(R[i])):
               # print(" R[i][j] = " , R[i][j])
                if len(NotReached)>0:
                    if R[i][j] in NotReached: #single node
                        #print('NotREached = ',NotReached , "R[i][j] = ",R[i][j])
                        NotReached.remove(R[i][j])
                        change = True
                        if len(NotReached) == 0:
                           break
                    else:               #non single node
                        #print("len(R[i][j]",len(R[i][j]))
                        for k in range(len(R[i][j])):
                           # print(k)
                            #print(" R[i][j][k] = ", R[i][j][k])
                            if R[i][j][k] in NotReached:
                                NotReached.remove(R[i][j][k])
                                change = True
                            if len(NotReached) == 0:
                                    break
                            else:
                                #print("finding indirect reachables")
                                #print(" R[i][j][k] = ", R[i][j][k])
                                if R[i][j][k] in V and R[i][j][k] in L:
                                    index = L.index(R[i][j][k])
                                   # print('checking production number ' ,index)
                                    for node in R[index]:
                                        for char in node:
                                            if char in NotReached:
                                                NotReached.remove(char)
                                                change = True
                                                if len(NotReached) == 0:
                                                    break

    if len(NotReached)>0:
        for p in NotReached:
            if p in L:
                L.remove(p)
            V.remove(p)
    return change



#------------------------------------------------------------------------------------
#####################entering and checking the productions#######################################
while len(p)>0:
    p = input('Enter the production rules (Enter to end)')
    if checkProduction(p):
        S.append(p)

while len(p)>0:
    check = True
    if check:
        for v in V:
            if not v in L:
                print('Enter the production rule for : ', v)
                p = input()
                if checkProduction(p):
                    S.append(p)
                    check = False
splitNodes()
#------------------------------------------------------------------------------------
#####################reducing the productions#######################################
output = True

while output and valid:

       if valid:
        checkEpsilon()
        valid =checkInvalid()

        if valid:
            output = checkUnit()
            valid = checkInvalid()

        if valid:
            output = checkUnReachable()
            valid =checkInvalid()

       if valid:
        output = checkUseLess()
        valid = checkInvalid()



# def removeDuplicates():
#     temp = []
#     for i in range(len(L)):
#         Ri = []
#         for j in range(len(R[i])-1,-1,-1):
#             if not R[i][j] in Ri:
#                 Ri.append(R[i][j])
#         temp.append(Ri)
#     R = temp
#------------------------------------------------------------------------------------
#output = checkUnit()
#output = checkEpsilon()

#


#print('L = ' , L)
#print('R = ' , R)
#print('{T} = ',T,end='\n')
#print('{V} = ',V,end='\n')
#print('{S} = ',S,end='\n')
if valid:
    printFinal()

else:
    print('Given grammar is invalid i.e no possible productions')
#------------------------------------------------------------------------------------

