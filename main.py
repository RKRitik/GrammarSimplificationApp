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
#####################productions simplification #######################################
def checkEpsilon():#check if e is in any of non starting symbols
    change = False
    for i in range(len(L)):
        if not L[i]==start_symbol:
            if epsilon_symbol in R[i]: #checking if RHS contains epsilon
                print('epsilon found ')
                change = True
                #substituting for e in current  non-terminal
                for j in  range(len(L)): #replacing this non terminal in other production
                    # if L[j]==start_symbol:
                    #     if epsilon_symbol not in R[j] :
                    #         result = False # checking if the non terminal with epsilon is present in start_prodection
                    #         for char in R[j]:
                    #             if char==L[i] :
                    #                 result = True
                    #             if result :
                    #                 R[j].append(epsilon_symbol)
                    #         else:
                    #             continue #avoiding wastage of  memory

                    print('R[j] = ',R[j])
                    len_ = len(R[j])
                    print(len_)
                    flag = False
                    for k in range(len_ - 1, -1,-1):  # traversing through each node in RHS to find the non terminal uses
                        print('k = ',k)
                        n = (R[j][k])
                        print(R[j][k])

                    for z in range(0,len(n)):
                        flag = True
                        print('n =',n)
                        n = list(n)
                        print('list(n) =',n)
                        temp = n
                        print('z = ', z , ' i = ', i , 'n = ', n , ' L = ',L)
                        if n[z] == L[i]:
                            del n[z]

                        print(n)
                        flag = fun(j,i,n)
                        n = temp  # restoring

                    if  flag and L[j]==start_symbol and not epsilon_symbol in R[j]:
                        R[j].append(epsilon_symbol)
                    if epsilon_symbol in R[j] and not L[j] == start_symbol:
                        R[j].remove(epsilon_symbol)

    print('new Productions : ')
    for i in range(len(L)):
        print(L[i],'->' , R[i])





    return change
def fun(j,i,n):
        flag = False
        while n.count(L[i]) > 0:
            flag = True
            print(n)
            n = list(n)
            n.remove(L[i])  # refactor
            n = list(n)
            print('n before  = ', n)
            # print(''.join(n)) #refactor this
            print('n after joining = ', n)
            if not n in R[j]:
                R[j].append(''.join(n))
        return flag
def checkUnit():
    change = False
    for i in range(len(L)):
        for j in range(len(R[i])):
            if len (R[i][j])==1 and R[i][j] in V: #finding the unit production
                change= True
                val = R[i][j]
                R[i].remove(val) #removing the unit production from production rules
                in_ = L.index(val)
                for node in R[in_]:
                    if node in T or len(node)>1: #checking if the rhs if a terminal or its lenth is greater than 1
                        #R[i].extend(node)
                        R[i].append(''.join(node))

    return change
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

    return

#------------------------------------------------------------------------------------
#####################entering and checking the productions#######################################
while len(p)>0:
    p = input('Enter the production rules (Enter to end)')
    if checkProduction(p):
        S.append(p)
splitNodes()
#------------------------------------------------------------------------------------
#####################reducing the productions#######################################
# change = True
# if output:
#     output = checkEpsilon()
#     output = checkUnit()
#     m m
#     output = checkUnReachable()

#------------------------------------------------------------------------------------


# output = checkEpsilon()

# output = checkUnit()
output = checkUseLess()
print('L = ' , L)
print('R = ' , R)
print('{T} = ',T,end='\n')
print('{V} = ',V,end='\n')
print('{S} = ',S,end='\n')
printFinal()
#------------------------------------------------------------------------------------

