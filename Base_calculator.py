# autor: NEGRU ALEXANDRU GEORGE

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def TransformareNrInLitere(n):
    if(n==10): return "A"
    if(n==11): return "B"
    if(n==12): return "C"
    if(n==13): return "D"
    if(n==14): return "E"
    if(n==15): return "F"
    return n

def TransformareLitereInNr(n):
    if(n == "A"): return 10
    if(n == "B"): return 11
    if(n == "C"): return 12
    if(n == "D"): return 13
    if(n == "E"): return 14
    if(n == "F"): return 15
    return n

   


  
def NrAltaBazaIn10(n,baza):
    #lucreaza cu sir nu cu nr
    #substitutie
    sum=0
    nr=n
    nr.reverse()
    for l in range(len(nr)): # merge de la 0 la len(Nlist)-1
        sum=int(nr[l])*(int(baza)**l)+sum
    return sum



def Nrbaza10InAltaBaza(n,baza):
    #lucreaza cu numar nu cu sir
    
    list=[]
    i=0
    n=int(n)
    while(n):
        list.append(str(TransformareNrInLitere(n%baza)))
        n=n//baza
        i=i+1
    list.reverse()
    nr = "".join(list) #imi concateneaza lista intr un string
    
    return nr




def conv_rapide(n,baza,baza_dorita):
    m=n
    for i in range(len(m)):
        m[i] = TransformareLitereInNr(m[i]) 
    #print(baza)
    for i in range(len(m)): # o sa am un elemnt din lista care e int (ex: A transformat in 10)
        m[i] = str(m[i])
    #print(m)
    a="".join(m)# imi concatenez lista intr un string
   # print(a + " aaaaaaaaaaaaaaa")
    nrn=''
    if(baza ==2):
        if (baza_dorita==2):
            nrn=a
        elif(baza_dorita==4):
            if(not(len(a)%2==0)):
                a=a[::-1]
                a=a+"0"
                a=a[::-1]
            for i in range(0,len(n),2):
                if(a[i]+a[i+1] =="00"):
                    nrn=nrn+'0'
                if(a[i]+a[i+1] =="01"):
                    nrn=nrn+'1'
                elif(a[i]+a[i+1] =="10"):
                    nrn=nrn+'2'
                elif(a[i]+a[i+1] =="11"):
                    nrn=nrn+'3'
        elif(baza_dorita==8):
           if(not(len(a)%3==0)):
                a=a[::-1]
                while(not(len(a)%3==0)):
                    a=a+"0"
                a=a[::-1]
           for i in range(0,len(n),3):
               if(a[i]+a[i+1]+a[i+2]=="000" and i!=0):
                   nrn = nrn+'0'
               if(a[i]+a[i+1]+a[i+2]=="001"):
                   nrn = nrn+'1'
               if(a[i]+a[i+1]+a[i+2]=="010"):
                   nrn = nrn+'2'
               if(a[i]+a[i+1]+a[i+2]=="011"):
                   nrn = nrn+'3'
               if(a[i]+a[i+1]+a[i+2]=="100"):
                   nrn = nrn+'4'
               if(a[i]+a[i+1]+a[i+2]=="101"):
                   nrn = nrn+'5'
               if(a[i]+a[i+1]+a[i+2]=="110"):
                   nrn = nrn+'6'
               if(a[i]+a[i+1]+a[i+2]=="111"):
                   nrn = nrn+'7'
        elif(baza_dorita==16):
           if(not(len(a)%4==0)):
                a=a[::-1]
                while(not(len(a)%4==0)):
                    a=a+"0"
                a=a[::-1]            
           for i in range(0,len(n),4):
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0000" and i!=0):
                    nrn = nrn+'0'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0001"):
                    nrn = nrn+'1'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0010"):
                    nrn = nrn+'2'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0011"):
                    nrn = nrn+'3'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0100"):
                    nrn = nrn+'4'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0101"):
                    nrn = nrn+'5'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0110"):
                    nrn = nrn+'6'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="0111"):
                    nrn = nrn+'7'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1000"):
                    nrn = nrn+'8'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1001"):
                    nrn = nrn+'9'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1010"):
                    nrn = nrn+'A'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1011"):
                    nrn = nrn+'B'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1100"):
                    nrn = nrn+'C'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1101"):
                    nrn = nrn+'D'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1110"):
                    nrn = nrn+'E'
                if(a[i]+a[i+1]+a[i+2]+a[i+3]=="1111"):
                    nrn = nrn+'F'
        
    elif(baza==4):
        if(baza_dorita==2):
            for i in range(0,len(n)):
                if(a[i]=="0" and i!=0):
                    nrn=nrn+"00"
                if(a[i]=="1"):
                    nrn=nrn+"01"
                if(a[i]=="2"):
                    nrn=nrn+"10"
                if(a[i]=="3"):
                    nrn=nrn+"11"
        else:
            print("nu ai introdus bine baza dorita sau numarul ")
            return 0
                 

    elif(baza==8):
        if(baza_dorita==2):
            for i in range(0,len(n)):
                if(a[i]=="0" and i!=0):
                    nrn=nrn+"000"
                if(a[i]=="1"):
                    nrn=nrn+"001"
                if(a[i]=="2"):
                    nrn=nrn+"010"                            
                if(a[i]=="3"):
                    nrn=nrn+"011"
                if(a[i]=="4"):
                    nrn=nrn+"100"  
                if(a[i]=="5"):
                    nrn=nrn+"101"
                if(a[i]=="6"):
                    nrn=nrn+"110"                            
                if(a[i]=="7"):
                    nrn=nrn+"111"
        else:
            print("nu ai introdus bine baza dorita sau numarul ")
            return 0
                
    elif(baza==16):
        for i in range(len(m)):
            m[i] = TransformareNrInLitere(int(m[i]))
        #print(m)
        for i in range(len(m)):
            m[i] = str(m[i])
        #print(m)
        a = "".join(m)
        if(baza_dorita==2):
            for i in range(0,len(n)):
                if(a[i]=="0" and i!=0):
                    nrn=nrn+"0000"
                if(a[i]=="1"):
                    nrn=nrn+"0001"
                if(a[i]=="2"):
                    nrn=nrn+"0010"                            
                if(a[i]=="3"):
                    nrn=nrn+"0011"
                if(a[i]=="4"):
                    nrn=nrn+"0100"  
                if(a[i]=="5"):
                    nrn=nrn+"0101"
                if(a[i]=="6"):
                    nrn=nrn+"0110"                            
                if(a[i]=="7"):
                    nrn=nrn+"0111"
                if(a[i]=="8"):
                    nrn=nrn+"1000"
                if(a[i]=="9"):
                    nrn=nrn+"1001"                            
                if(a[i]=="A"):
                    nrn=nrn+"1010"
                if(a[i]=="B"):
                    nrn=nrn+"1011"  
                if(a[i]=="C"):
                    nrn=nrn+"1100"
                if(a[i]=="D"):
                    nrn=nrn+"1101"                            
                if(a[i]=="E"):
                    nrn=nrn+"1110"
                if(a[i]=="F"):
                    nrn=nrn+"1111"
        else:
            print("nu ai introdus bine baza dorita sau numarul ")
            return 0                    


                    
    else:
        print("nu ai introdus bine baza dorita sau numarul ")
        return 0

    print(nrn)            

    
    
    
def baza_intermediara(n,baza,baza_destinatie):
    #il trec din baza curenta in baza 10
    #dupa din baza 10 il trec in baza destinatie
    baza_destinatie = int(baza_destinatie)
    n=str(n)       
    Nlist = [i for i in n]
   # print(Nlist)
    for i in range(len(Nlist)):
        Nlist[i] = str(TransformareLitereInNr(Nlist[i]))
    nr = NrAltaBazaIn10(Nlist,baza)
    
    
    return (Nrbaza10InAltaBaza(nr,baza_destinatie))



def adunare(nr1,baza1,nr2,baza2,baza_adunare):
    nr1=int(nr1)
    nr2=int(nr2)
    baza1=int(baza1)
    baza2=int(baza2)
    if(nr1==0 and nr2==0):
        print("rezultatul este: 0")
        return 0
    if(nr2==0):
        print("rezultatul este: "+str(nr1))
        return 0
    if(nr1==0):
        print("rezultatul este: "+str(nr2))
        return 0
    n1=baza_intermediara(nr1,baza1,baza_adunare)
    n2=baza_intermediara(nr2,baza2,baza_adunare)
    #print(n1) # imi afisez numarul
   # print(n2)
    
    n1=str(n1)#convertesc numerele la string deoarece imi e mai usor sa lucrez asa cu ele
    n2=str(n2)
    baza_adunare = int(baza_adunare)
    
    nr1 = [i for i in n1]#BAG NUMERELE IN LISTA, deoarece imi e mai usor sa lucrez asa
    nr2 = [i for i in n2]
   # print(nr1)
   # print(nr2)
    
    
    if(len(nr1) > len(nr2)):
        k=len(nr1)
    else:
        k=len(nr2)
        
   # print(k)
   # print("LLKKKKKKKKKKK")
    #lucrez cu nuamrul intros deoarece vreau sa incep cu unitatile iar [::-1] imi intoarce lista
    nr1=nr1[::-1]
    nr2=nr2[::-1]

    for i in range(len(nr1)):
        nr1[i]= TransformareLitereInNr(nr1[i])
    for i in range(len(nr2)):
        nr2[i]= TransformareLitereInNr(nr2[i])
    
    nr3=[]
    t=[]
    t.append(0)
    for i in range(k):
       t.append(int((int(nr1[i])+int(nr2[i])+t[i])/baza_adunare))
       nr3.append((int(nr1[i])+int(nr2[i])+t[i])%baza_adunare)
       #print(t[i+1])    aici am aplicat alogritmul de adunare in diferite baze
       #print(nr3)
        
    if(t[k]!=0):
       #nr3[len(k)]=t[len(k)]     aici verific daca exista un element unitate mai mare decat K si daca exista il adaug noului numar
       nr3.append(t[k])

       #intorc nuamrul 
    nr3 = nr3[::-1]

    
    
    for i in range(len(nr3)):
        nr3[i]=TransformareNrInLitere(nr3[i]) # in caz ca am baza mai mare ca 10 imi transform cifrele in Litere
        nr3[i]= str(nr3[i]) # imi convertesc numerele la string deoarece vreau ca lista sa o transform intr un string
    nr ="".join(nr3)
    print(nr)
   #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
def adunare1(nr1,baza1,nr2,baza2,baza_adunare):
    
    baza1=int(baza1)
    baza2=int(baza2)
    if(nr1==0 and nr2==0):
        print("rezultatul este: 0")
        return 0
    if(nr2==0):
        print("rezultatul este: "+str(nr1))
        return 0
    if(nr1==0):
        print("rezultatul este: "+str(nr2))
        return 0
    n1=baza_intermediara(nr1,baza1,baza_adunare)
    n2=baza_intermediara(nr2,baza2,baza_adunare)
   
    
    n1=str(n1)#convertesc numerele la string deoarece imi e mai usor sa lucrez asa cu ele
    n2=str(n2)
    baza_adunare = int(baza_adunare)
    
    nr1 = [i for i in n1]#BAG NUMERELE IN LISTA, deoarece imi e mai usor sa lucrez asa
    nr2 = [i for i in n2]
    
    
    if(len(nr1) > len(nr2)):
        nrmax=nr1
    else:
        nrmax=nr2 #  mi am salvat un nr max deoarece daca adun si cumva t[k] este diferit de 0 atunci imi trebuie pozitia urmatoare a numarului cel mai mare ca sa pot sa adun unitatea

    
    if(len(nr1) < len(nr2)):
        k=len(nr1)
    else:
        k=len(nr2)
        
    
    #lucrez cu nuamrul intros deoarece vreau sa incep cu unitatile iar [::-1] imi intoarce lista
    nr1=nr1[::-1]
    nr2=nr2[::-1]
    nrmax=nrmax[::-1]  #le am intros invers
    for i in range(len(nr1)):
        nr1[i]= TransformareLitereInNr(nr1[i])
    for i in range(len(nr2)):
        nr2[i]= TransformareLitereInNr(nr2[i])
    for i in range(len(nrmax)):
        nrmax[i]= TransformareLitereInNr(nrmax[i])
   
    nr3=[]
    t=[]
    t.append(0)
    for i in range(k):
       t.append(int((int(nr1[i])+int(nr2[i])+t[i])/baza_adunare))
       nr3.append((int(nr1[i])+int(nr2[i])+t[i])%baza_adunare)
       #print(t[i+1])    aici am aplicat alogritmul de adunare in diferite baze
       #print(nr3)
    if(t[k]!=0):

           #nr3[len(k)]=t[len(k)]     aici verific daca exista un element unitate mai mare decat K si daca exista il adaug noului numar
           #in caz ca unitatea creste iar o tot  cresc pana ajung la capatul numarului
        ok=1
        nr3.append(t[k]+int(nrmax[k]))
        
        while(k<len(nrmax)-1):
                                                    #for l in range(k,len(nrmax)):
            if(int(nr3[k])==baza_adunare):
                nr3[k]=0
                k=k+1
                nr3.append(1+int(nrmax[k]))
            else:
                k=len(nrmax)

        
        m=len(nr3)
        if(int(nr3[m-1]) ==baza_adunare):
            nr3[m-1]=0
            m=m+1
            nr3.append(1)
        for i in range(m,len(nrmax)):
            nr3.append(nrmax[i])
    else:
        m=len(nr3)
        for i in range(m,len(nrmax)):
            nr3.append(nrmax[i])

    #print(nr3)
    # aici trebuie


       #intorc nuamrul 
    nr3 = nr3[::-1]
    for i in range(len(nr3)):
        nr3[i]=TransformareNrInLitere(nr3[i]) # in caz ca am baza mai mare ca 10 imi transform cifrele in Litere
        nr3[i]= str(nr3[i]) # imi convertesc numerele la string deoarece vreau ca lista sa o transform intr un string
    nr ="".join(nr3)
    print(nr)

#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    #TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
#adunare1(10,10,9,10,10)


    

def scadere(nr1,baza1,nr2,baza2,baza_scadere):
    
    baza1=int(baza1)
    baza2=int(baza2)
    if(nr1==0 and nr2==0):
        print("rezultatul este: 0")
        return 0
    elif(nr1==0):
        print("rezultatul  este: " + str(nr2))
        return 0
    elif(nr2==0):
        print("rezultatul  este: " + str(nr1))
        return 0
    n1=baza_intermediara(nr1,baza1,baza_scadere)
    n2=baza_intermediara(nr2,baza2,baza_scadere)
    #print(n1) # imi afisez numarul
    #print(n2)
    
    n1=str(n1)#convertesc numerele la string deoarece imi e mai usor sa lucrez asa cu ele
    n2=str(n2)
    baza_scadere = int(baza_scadere)
    
    nr1 = [i for i in n1]#BAG NUMERELE IN LISTA, deoarece imi e mai usor sa lucrez asa
    nr2 = [i for i in n2]
    
    
    
    if(len(nr1) > len(nr2)):
        k=len(nr1)
    else:
        k=len(nr2)
        
    for i in range(len(nr1)):
        nr1[i]= TransformareLitereInNr(nr1[i])
        nr1[i] = int(nr1[i])
    for i in range(len(nr2)):
        nr2[i]= TransformareLitereInNr(nr2[i])
        nr2[i] = int(nr2[i])

    if(len(nr1)<len(nr2)):
        aux=nr1
        nr1=nr2
        nr2=aux
    elif((len(nr1)==len(nr2)) and (int(nr1[0])<int(nr2[0]))):#verific care numar este mai mare, ca sa stiu ce descazut si  scazator am(nr1 descazut tot timpul=> nr2 scazator)
        aux=nr1
        nr1=nr2
        nr2=aux
    
        
    #lucrez cu nuamrul intros deoarece vreau sa incep cu unitatile iar [::-1] imi intoarce lista
    nr1=nr1[::-1]
    nr2=nr2[::-1]
    nr3=[]
    t=[]
    t.append(0)
    for i in range(k):
        if(i<=len(nr2)-1):
            if(nr1[i]+t[i]>= nr2[i]):
                nr3.append(nr1[i]+t[i]-nr2[i])
                t.append(0)
                
            else:
                nr3.append(baza_scadere+nr1[i]+t[i]-nr2[i])
                t.append(-1)
                

        else:
            i=k
    m=len(nr2)
    if(t[m]==-1):
        ok=1
        while(ok):
            nr3.append(int(t[m]) +int(nr1[m]))
            if(not(nr3[m]==-1)):
                ok=0
            else:
                m=m+1
        
            
        for i in range(m+1,len(nr1)):
            nr3.append(nr1[i])

    else:
        for i in range(len(nr2),len(nr1)):
            nr3.append(nr1[i])

    while(nr3[len(nr3)-1]==0):
        del nr3[-1]
    
        
#intorc nuamrul 
    nr3 = nr3[::-1]

    
    
    for i in range(len(nr3)):
        nr3[i]=TransformareNrInLitere(nr3[i]) # in caz ca am baza mai mare ca 10 imi transform cifrele in Litere
        nr3[i]= str(nr3[i]) # imi convertesc numerele la string deoarece vreau ca lista sa o transform intr un string
    nr ="".join(nr3)
    print(nr)       

def inmultire(nr1,baza1,nr2,baza2,baza_inmultire):
    
    baza1=int(baza1)
    baza2=int(baza2)
    if(nr1==0):
        print("produsul este 0")
        return 0
    if(nr2==0):
        print("produsul este 0")
        return 0
    n1=baza_intermediara(nr1,baza1,baza_inmultire)
    n2=baza_intermediara(nr2,baza2,baza_inmultire)
    #print(n1) # imi afisez numarul
    #print(n2)
  
    baza_inmultire = int(baza_inmultire)
    
    
    
    n1=str(n1)#convertesc numerele la string deoarece imi e mai usor sa lucrez asa cu ele
    n2=str(n2)
    
    
    nr1 = [i for i in n1]#BAG NUMERELE IN LISTA, deoarece imi e mai usor sa lucrez asa
    nr2 = [i for i in n2]
    

    
    if(len(nr1) > len(nr2)):
        k=len(nr1)
    else:
        k=len(nr2)
        
    for i in range(len(nr1)):
        nr1[i]= TransformareLitereInNr(nr1[i])
        nr1[i] = str(nr1[i])
    for i in range(len(nr2)):
        nr2[i]= TransformareLitereInNr(nr2[i])
        nr2[i] = str(nr2[i])

    # le am convertit in string ca sa pot sa verific daca am o cifra. Daca am cifra, pot face inmultirea
        n1="".join(nr1)
        n2="".join(nr2)
        n1=int(n1)
        n2=int(n2)
    
    if(n1>9 and n2>9):
        print("nu ai introdus o cifra...")
        return 0

    
    for i in range(len(nr1)):
        nr1[i] = int(nr1[i])
    for i in range(len(nr2)):
        nr2[i] = int(nr2[i])

   
    
        
    if(len(nr1)<len(nr2)): #verific care numar este mai mare, ca sa stiu cum le inmultesc)
        aux=nr1
        nr1=nr2
        nr2=aux

        
    #lucrez cu nuamrul intros deoarece vreau sa incep cu unitatile iar [::-1] imi intoarce lista
    nr1=nr1[::-1]
    nr2=nr2[::-1]
    nr3=[]
    t=[]
    t.append(0)
    for i in range(k):
        t.append(int((nr1[i]*nr2[0]+t[i])/baza_inmultire))
        nr3.append((nr1[i]*nr2[0]+t[i])%baza_inmultire)
    if(t[k]!=0):
       nr3.append(t[k])


    #intorc nuamrul 
    nr3 = nr3[::-1]

    
    
    for i in range(len(nr3)):
        nr3[i]=TransformareNrInLitere(nr3[i]) # in caz ca am baza mai mare ca 10 imi transform cifrele in Litere
        nr3[i]= str(nr3[i]) # imi convertesc numerele la string deoarece vreau ca lista sa o transform intr un string
    nr ="".join(nr3)
    print(nr)



def impartire(nr1,baza1,nr2,baza2,baza_impartire):
    
    baza1=int(baza1)
    baza2=int(baza2)
    if(nr1==0 and nr2<=9):
        print("rezultatul este: 0")
        return 0
    if(nr2==0 and nr1<=9):
        print("rezultatul este: 0")
        return 0
    elif(nr1==0 and nr2>9):
        print("nu se poate imparti cu 0")
        return 0
    elif(nr2==0 and nr1>9):
        print("nu se poate imparti cu 0")
        return 0

    
    n1=baza_intermediara(nr1,baza1,baza_impartire)
    n2=baza_intermediara(nr2,baza2,baza_impartire)
    #print(n1) # imi afisez numarul
    #print(n2)
  
    baza_impartire = int(baza_impartire)
    
    
    
    n1=str(n1)#convertesc numerele la string deoarece imi e mai usor sa lucrez asa cu ele
    n2=str(n2)
    
    
    nr1 = [i for i in n1]#BAG NUMERELE IN LISTA, deoarece imi e mai usor sa lucrez asa
    nr2 = [i for i in n2]
    

    
    if(len(nr1) > len(nr2)):
        k=len(nr1)
    else:
        k=len(nr2)
        
    for i in range(len(nr1)):
        nr1[i]= TransformareLitereInNr(nr1[i])
        nr1[i] = str(nr1[i])
    for i in range(len(nr2)):
        nr2[i]= TransformareLitereInNr(nr2[i])
        nr2[i] = str(nr2[i])

    # le am convertit in string ca sa pot sa verific daca am o cifra. Daca am cifra, pot face impartirea
        n1="".join(nr1)
        n2="".join(nr2)
        n1=int(n1)
        n2=int(n2)
    
    if(n1>9 and n2>9):
        print("nu ai introdus o cifra...")
        return 0

    
    for i in range(len(nr1)):
        nr1[i] = int(nr1[i])
    for i in range(len(nr2)):
        nr2[i] = int(nr2[i])

   
    
        
    if(len(nr1)<len(nr2)): #verific care numar este mai mare, ca sa stiu cum le imaprt (care  e numitor si care e numarator).
        aux=nr1
        nr1=nr2
        nr2=aux
        


    elif(len(nr1)==len(nr2)):
        if(nr1[0]<nr2[0]):
            aux=nr1
            nr1=nr2
            nr2=aux
# il aleg pe nr1 ca numarator
        
    #lucrez cu nuamrul intros deoarece vreau sa incep cu unitatile iar [::-1] imi intoarce lista
    #nr1=nr1[::-1]
    #nr2=nr2[::-1]
    nr3=[]
    t=[]
    t.append(0)
    for i in range(k):
        t.append((t[i]*baza_impartire+nr1[i])%nr2[0])
        nr3.append(int((t[i]*baza_impartire+nr1[i])/nr2[0]))

   #aici nu mai trebuie sa intorc numarul deoarece am inceput sa imaprt de la unitatea cea mai mare (de la dreapta la stanga)

    
    
    for i in range(len(nr3)):
        nr3[i]=TransformareNrInLitere(nr3[i]) # in caz ca am baza mai mare ca 10 imi transform cifrele in Litere
        nr3[i]= str(nr3[i]) # imi convertesc numerele la string deoarece vreau ca lista sa o transform intr un string
    if(nr3[0]=="0"):
        del nr3[0:1]
        
    nr ="".join(nr3)
    print(str(nr) + " rest " + str(t[k]))   
    return str(nr),str(t[k])

"""
def impartiriSuccesive(n1,baza,baza_destinatie):
    if(baza == baza_destinatie):
        return n1
    list=[]
    i=0
    cat=n1
    while(cat!=0):
        cat,rest=impartire(cat,baza,baza_destinatie,baza_destinatie)
        list.append(rest)
    list=list[::1]
    print(list)


impartiriSuccesive(123,4,10)
"""
def citirenr1():
    ok=1
    ok1=1
    da=1
    while(da):
        ok=1
        while(ok):
            ok1=1
            n1 = input("introduceti primul numar: ")
            bn1 = input("introduceti baza in care se afla numarul: ")
            N1list = [i for i in n1] #imi baga fiecare element din nr intr o lista
            if(not isfloat(bn1)):
                ok1=0
                print("ai introdus o baza gresita")
            elif(not(int(bn1)>=2 and int(bn1)<=16)):
                ok1=0
            
                print("ai introdus o baza gresita")
            else:
                for j in range(len(N1list)):
                    if(TransformareLitereInNr(N1list[j])):
                        N1list[j] = TransformareLitereInNr(N1list[j])
                    if(not isfloat(N1list[j])):  #verific daca numarul este intreg sau float
                        print("NUMARUL INTRODUS ESTE GRESIT... mai incearca ")
                        j=len(N1list)+1
                        ok1=0
                        break
                
                    elif(int(N1list[j])>=int(bn1) or int(N1list[j])<0):
                        print("ai introdus o baza gresita")
                        j=len(N1list)+1
                        ok1=0
                        break
         
            if(ok1==0):
                #print("AI INTRODUS GRESIT NUMARUL SAU BAZA")
                ok=0
            else:
                ok=0
                da=0
    bn1=int(bn1)
    return n1,N1list,bn1

def citirenr2():
    
    ok=1
    ok1=1
    da=1
    while(da):
        ok=1
        while(ok):
            ok1=1
            n2 = input("introduceti al doilea numar: ")
            bn2 = input("introduceti baza in care se afla numarul: ")
            N1list = [i for i in n2] #imi baga fiecare element din nr intr o lista
            if(not isfloat(bn2)):
                ok1=0
                print("ai introdus o baza gresita")
            elif(not(int(bn2)>=2 and int(bn2)<=16)):
                ok1=0
                print("ai introdus o baza gresita")
            else:
                for j in range(len(N1list)):
                    if(TransformareLitereInNr(N1list[j])):
                        N1list[j] = TransformareLitereInNr(N1list[j])
                    if(not isfloat(N1list[j])):  #verific daca numarul este inreg sau float
                        print("NUMARUL INTRODUS ESTE GRESIT... mai incearca ")
                        j=len(N1list)+1
                        ok1=0
                        break
                
                    elif(int(N1list[j])>=int(bn2) or int(N1list[j])<0):
                        print("ai introdus o baza gresita")
                        ok1=0
    
            if(ok1==0):
                #print("AI INTRODUS GRESIT NUMARUL SAU BAZA")
                ok=0
            else:
                ok=0
                da=0
    
    bn2= int(bn2)
    return n2,N1list,bn2


def baza_destinatie():
  ok=1
  while(ok):
    n=input("introdu baza destinatie: ")
    if(not isfloat(n)):
        print("nu ai introdus o baza corecta")
        
    elif not(isInt(n) and (int(n)>0 and int(n)<=16)):
        print("nu ai introdus o baza corecta :(")
    else:
        ok=0
  n=int(n)
  return n
      
      


def listaOptiuni():
    print("autor:NEGRU ALEXANDRU GEORGE")
    print("CE POTI FACE IN ACEST PROGRAM :)")
    print("1 ->SCHIMBA UN NR DIN BAZA 10 IN ALTA BAZA")
    print("2 ->SCHIMBA UN NR DIN ORICE BAZA IN BAZA 10")
    print("3 ->FACE CONVERSIE PRIN IMPARTIRI SUCCESIVE")
    #print("4 ->FACE CONVERSIE PRIN SUBSTITUTIE")
    print("4 ->FACE CONVERSIE PRIN COVNERSII RAPIDE")
    print("5 ->FACE CONVERSIE UTILIZAND O BAZA INTERMEDIARA")
    print("6 ->FACE ADUNARI, SCADERI,IMPARTIRI, INMULTIRI, INTRE DOUA NUMERE")
    n=input("alege optiunea: ")
    return n


def introdu_pt_cerinta_1():
    ok=1
    da=1
    ok1=1
    while (da):
        ok=1
        while(ok):
            ok1=1
            n=input("introdu un nr in baza 10: ")
            if(n=="0"):
                ok1=0
                da=0
                break
            if(n==""):
                ok1=0
                print("nu ai introdus bine")
            
            Nlist = [i for i in n]

            for i in range(len(Nlist)):
                if(not isfloat(Nlist[i])):  #verific daca numarul este intreg sau float
                            print("NUMARUL INTRODUS ESTE GRESIT... mai incearca .")
                            i=len(Nlist)+1
                            ok1=0
                            break
                elif not(int(Nlist[i])>=0 and int(Nlist[i])<=9):
                    print("numarul introdus este gresit...mai incearca")
                    i=len(N1list)+1
                    ok1=0
                    break

            if(ok1==0):    
             ok=0
            else:
                ok=0
                da=0
                
    ok=1
    while(ok):
        b =input("intrdoduceti baza in care vreti sa se faca conversia: ")
        if(not isfloat(b)):
            print("ai introdus ceva gresit... incearca alta baza")
        elif not(int(b)>=2 and int(b)<=16):
            print("ai introdus ceva gresit... incearca alta baza")
        else:
            ok=0

    n=int(n)
    b=int(b)
    return n,b


    


def sugetie_baza(n):
    n=int(n)
    if(n==2):
        print("alege baza : 2, 4, 8 sau 16")
    if(n==4):
        print("TASTEAZA 2 PENTRU A TRANSFORMA NR IN BAZA 2")
    if(n==8):
        print("TASTEAZA 2 PENTRU A TRANSFORMA NR IN BAZA 2")
    if(n==16):
        print("TASTEAZA 2 PENTRU A TRANSFORMA NR IN BAZA 2")

def varianta6():
    print()
    print("introduceti din nou ce vreti sa faceti :")
    print("1-> pentru adunari")
    print("2-> pentru scaderi")
    print("3-> pentru inmultiri")
    print("4 -> pentru impartiri")
    n=input("introduceti: ")      
    return n   

def alegereOptiuni(optiune):
    ok=1
    while ok :
        
        if(optiune=="1"):
            n,b=introdu_pt_cerinta_1()
            print(Nrbaza10InAltaBaza(n,b))
            ok=0
            
            
        elif(optiune =="2"):
            n1,N1list,bn1=citirenr1()
            print(NrAltaBazaIn10(N1list,bn1))
            ok=0

        elif(optiune=="3"):
            n,b=introdu_pt_cerinta_1()
            print(Nrbaza10InAltaBaza(n,b))
            ok=0
        elif(optiune =="4"):
        	print("Introduceti un nr din baza 2,4,8 sau 16 pentru conversii rapide ")
        	n1,N1list,bn1=citirenr1()
        	sugetie_baza(bn1)
        	baza_dorita=baza_destinatie()
        	conv_rapide(N1list,bn1,baza_dorita)
        	ok=0
        elif(optiune =="5"):
            n1,N1list,bn1=citirenr1()
            baza_dorita=baza_destinatie()
            print(baza_intermediara(n1,bn1,baza_dorita))
            ok=0

        elif(optiune =="6"):
            n=varianta6()
            ok=1
            while(ok):
                if(not isfloat(n)):
                    print("nu ai introdus ce trebuie... ")
                    n=input("reintrodu:")
                elif n=="1":
                    n1,N1list,bn1=citirenr1()
                    n2,N2list,bn2=citirenr2()
                    baza_dorita = baza_destinatie()
                    adunare1(n1,bn1,n2,bn2,baza_dorita)
                    ok=0
                elif n=="2":
                    n1,N1list,bn1=citirenr1()
                    n2,N2list,bn2=citirenr2()
                    baza_dorita = baza_destinatie()
                    scadere(n1,bn1,n2,bn2,baza_dorita)
                    ok=0
                elif n=="3":
                    n1,N1list,bn1=citirenr1()
                    n2,N2list,bn2=citirenr2()
                    baza_dorita = baza_destinatie()
                    inmultire(n1,bn1,n2,bn2,baza_dorita)
                    ok=0
                elif n=="4":
                    n1,N1list,bn1=citirenr1()
                    n2,N2list,bn2=citirenr2()
                    baza_dorita = baza_destinatie()
                    impartire(n1,bn1,n2,bn2,baza_dorita)
                    ok=0  
                
                else:
                    print("nu ai introdus ce trebuie...")
                    n=input("reintrodu: ")
          
        else:
            print("NU AI INTRODUS UNA DIN OPTIUNI... mai incearca")
            optiune = input("reintrodu: ")




            
#Kind of main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> main main main >>>>>>>>>>>>>>>>>>>>>>>
        #MAIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MAINMAINMAINMAINMAINMAINMAIN>>>>>>>>MAIN>MAIN>MAIN>MAIN>MAIN>>>>>>>>>>>>>>
            #main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> main main main >>>>>>>>>>>>>>>>>>>>>>>
        #MAIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MAINMAINMAINMAINMAINMAINMAIN>>>>>>>>MAIN>MAIN>MAIN>MAIN>MAIN>>>>>>>>>>>>>>


optiune=listaOptiuni()
alegereOptiuni(optiune)
input("TASTEAZA ORICE PENTRU A INCHIDE PROGRAMUL:  ")






