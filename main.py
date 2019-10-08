T = ['a','b']
V = ['A','B']
start_symbol = 'S'
epsilon_symbol = 'e'
S = []
L = [] #stores all the LHS of the production rules
R = [] #rhs of productions


#------------------------------------------------------------------------------------
# T = input('Enter the terminals ').split() # eg a b c do not put e as a terminal
# V = input('Enter the non-terminals ').split() # eg A B
# start_symbol = input('Enter the Start Symbol ')
# epsilon_symbol = input('Enter the Epsilon Symbol ')

#------------------------------------------------------------------------------------
V.append(start_symbol)
T.append(epsilon_symbol)
# check(T,V)
p = ' '
#------------------------------------------------------------------------------------
def printFinal():
    for l,r in zip(L,R):
        print(l,'->',r)
#------------------------------------------------------------------------------------
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
        if not L[i]==start_symbol:
            if epsilon_symbol in R[i]: #checking if RHS contains epsilon
                print('epsilon found ')
                change = True
                symbol = L[i]
                #substituting for e in current  non-terminal
                for j in  range(len(L)): #replacing this non terminal in other production
                    print('R[j] = ',R[j])
                    len_ = len(R[j])
                    print(len_)
                    flag = False
                    for k in range(len_ - 1, -1,-1):  # traversing through each node in RHS to find the non terminal uses
                        #print('k = ',k)
                        n = (R[j][k])
                        print(R[j][k])
                        n = list(n)
                        print('list(n) =', n)
                        temp = n
                        # print('z = ', z , ' i = ', i , 'n = ', n , ' L = ',L)
                        print('symbol = ',symbol," temp = ",temp)
                        if symbol in temp:
                            print('symbol present in node index ', k)
                            fun(symbol,temp,j,i,n)#recurcive function to find all combinations after substituting the symbol
                        #n = temp  # restoring

                    if  flag and L[j]==start_symbol and not epsilon_symbol in R[j]:
                        R[j].append(epsilon_symbol)
                    if epsilon_symbol in R[j] and not L[j] == start_symbol:
                        R[j].remove(epsilon_symbol)

    print('new Productions : ')
    for i in range(len(L)):
        print(L[i],'->' , R[i])





    return change
def fun(symbol,temp,j,i,n): ##refactored code from ishaaan
        print('fun called , temp = ',temp)
        if temp.count(symbol) > 0 :
            l = len(temp)
            for num in range(l - 1, -1,-1):
                if temp[num] == symbol:
                    temp1 = temp
                    del temp1[num]
                    print('extended temp1 = ',temp1 )
                    R[j].extend(temp1)
                    fun(symbol,temp1,j,i,n)

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
    #int_ = 0
    #lis = []
    for i in range(len(L)):
        values = []
        for j in range(len(R[i])-1,-1,-1):
              lis = []
             # print('R[i][j] = ',R[i][j])
              if  R[i][j] in V: #finding the unit production
                   change= True
                   val = R[i][j]
                   list_all.append(val)
                  # print('removing ',val)
                #   R[i].remove(val) #removing the unit production from production rules
                   #in_ = L.index(val)
                   values.extend(fun_(list_all))
                   list_all.clear()


        R[i].extend(values)
        list_all.clear()
        values.clear()

    for i in range(len(L)):
        temp = []
        for v in R[i]:
            if v in V:
                R[i].remove(v)
            else:
                if not v in temp:
                    temp.append(v)
        R[i] = temp
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
    print('list_all = ',list_all)
    values = []
    printFinal()
    for k in range(len(R)):# traversing through production rules
        if L[k] in list_all :#checking if the lhs 's values needs to be substituted
            for l in range(len(R[k])-1,-1,-1):
                if not R[k][l] in V:
                    values.append(R[k][l])
                    #R[k].remove(R[k][l])
    print('values = ',values)
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
    # print('R = ', R)
    for i in range(len(R)):
        for node in R[i]:
            if node in T:
                useful.append(L[i])
    #now check if any node in RHS is made of only one of these useful symbols
    for  i in range(len(R)):
        for node in R[i]:
            if  node in useful:
                useful.append(L[i])
    useLess = list(set(L)-set(useful))
    #removing the nodes the the productions containing useless non terminals
    # print('R = ', R)
    for u in useLess:
        for i in range(len(R)-1,-1,-1):
            print('i = ',i)
            for j in range(len(R[i])-1,-1,-1):
                print('j = ', j)
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
                                if R[i][j][k] in V :
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
            index = index = L.index(p)
            L.remove(p)
            pR = R[index]
            R.remove(pR)
    return change



#------------------------------------------------------------------------------------
#####################entering and checking the productions#######################################
while len(p)>0:
    p = input('Enter the production rules (Enter to end)')
    if checkProduction(p):
        S.append(p)
splitNodes()
#------------------------------------------------------------------------------------
#####################reducing the productions#######################################
output = True
# if output:
#      #output = checkEpsilon()#problems
#      output = checkUnit() #maybeproblems
#      output = checkUseLess()
#      output = checkUnReachable()

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
output = checkUnit()
#output = checkEpsilon()

#


#print('L = ' , L)
#print('R = ' , R)
#print('{T} = ',T,end='\n')
#print('{V} = ',V,end='\n')
#print('{S} = ',S,end='\n')

printFinal()

#------------------------------------------------------------------------------------

