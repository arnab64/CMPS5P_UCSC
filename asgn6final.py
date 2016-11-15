import os.path

def getfile(fname):
    if os.path.isfile(fname)==False:
        print("The file",fname,"is not present!")
        return None
    else:
        infile = open(fname)
        intext = infile.read()
        return intext
        
def preprocess(text):
    text = text.lower()
    print("length is:",len(text))
    newchar = []
    for chr in text:
        if chr.isspace()==True or chr.isalpha()==True:
            newchar.append(chr)
    newstr = "".join(newchar)
    return(newstr)
    
def centralupdate(elem,gram):
    if gram==1:
        for j,k in dictx['dict1'].items():
            if j==elem:
                #print("found",elem,"with count",k)
                dictx['dict1'].update({j:k+1})
                return(None)
        dictx['dict1'].update({elem:1})
    elif gram==2:
        for j,k in dictx['dict2'].items():
            if j==elem:
                #print("found",elem,"with count",k)
                dictx['dict2'].update({j:k+1})
                return(None)
        dictx['dict2'].update({elem:1})
    elif gram==3:
        for j,k in dictx['dict3'].items():
            if j==elem:
                #print("found",elem,"with count",k)
                dictx['dict3'].update({j:k+1})
                return(None)
        dictx['dict3'].update({elem:1})
    elif gram==123:
        for j,k in dictx['dictw'].items():
            if j==elem:
                #print("found",elem,"with count",k)
                dictx['dictw'].update({j:k+1})
                return(None)
        dictx['dictw'].update({elem:1})
    
def update1(listofsomegrams,grams):
    for big in listofsomegrams:
        centralupdate(big,grams)
    
def getngrams(word,n):
    ng = []
    for j in range(len(word)-n+1):
        ng.append(word[j:j+n])
    return(ng)
                
def countall(text):
    allgrams=[]
    words = text.split()
    update1(words,123)
    for k in range(1,4):
        for j in words:
            lol = getngrams(j,k)
            allgrams.extend(lol)
        #print(k,"grams are:",allgrams)
        #print("updating",allgrams,"with gram=",k)
        update1(allgrams,k)
        del allgrams[:]

def add_dicts(toupdate):
    listx = {'dictw','dict1','dict2','dict3'}
    if toupdate=='dictall':
        for dname in listx:
            for x in dictx[dname].keys():
                if x in dictall[dname].keys():
                    dictall[dname].update({x:dictx[dname][x]+dictall[dname][x]})
                else:
                    dictall[dname].update({x:dictx[dname][x]})
    elif toupdate=='dictx':
        for dname in listx:
            for x in dictx[dname].keys():
                if x in dictall[dname].keys():
                    dictx[dname].update({x:dictx[dname][x]+dictall[dname][x]})
                else:
                    dictx[dname].update({x:dictx[dname][x]})
    else:
        print("Come back again!")    
        
def gettop25():
    for elem in dnames:
        lot = []
        total = 0
        ofile.write("\n-------------"+elem+"---------------------\n")
        for j,k in dictx[elem].items():
            tupx = (j,k)
            lot.append(tupx)
            total = total+k
        #listv.append(total)
        lot.sort(key = lambda tup:tup[1], reverse=True)
        max1 = 25
        if len(lot)<25:
            max1=len(lot)
        for p in range(max1):
            axe = lot[p]
            print(axe[0],axe[1],str(round(axe[1]*100/float(total),2))+'%')
            ofile.write(str(axe[0])+"   "+str(axe[1])+" "+str(round(axe[1]*100/float(total),2))+"%\n")
        
def gettop():
    for elem in dictall.keys():
        print("\n-------------",elem,"---------------------")
        lot = []
        total = 0
        for j,k in dictall[elem].items():
            tupx = (j,k)
            lot.append(tupx)
            total = total+k
        lot.sort(key = lambda tup:tup[1], reverse=True)
        max1 = 25
        if len(lot)<25:
            max1=len(lot)
        for p in range(max1):
            axe = lot[p]
            print(axe[0],"  ",axe[1],"  ",str(round(axe[1]*100/float(total),2))+'%')
            ofile.write(str(axe[0])+"   "+str(axe[1])+" "+str(round(axe[1]*100/float(total),2))+"%\n")
        
dnames = ['dictw','dict1','dict2','dict3']
dictx = {'dictw':{},'dict1':{},'dict2':{},'dict3':{}}
dictall = {'dictw':{},'dict1':{},'dict2':{},'dict3':{}}
ofile = open('ofile.txt','w')

#inpx = input("Enter the names of text files with spaces in between")
inpx = 'one.txt dickens1.txt stevenson1.txt'
files = inpx.split()
total = 0
for fn in files:
    text1 = getfile(fn)
    text2 = preprocess(text1)
    countall(text2)
    print("-----------",fn,"-------------")
    ofile.write("\n-----------"+str(fn)+"-------------")
    print(gettop25())
    add_dicts('dictall')              #add the dictionaries
    for elem in dictx.keys():
        dictx[elem].clear()
    # dictx['dict1'].clear()
    # dictx['dict2'].clear()
    # dictx['dict3'].clear()
print("-------overall--------")
gettop()
    
    