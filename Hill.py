#Module qui sert à chiffrer/dechiffrer un message en utilisant le chiffrement de Hill



#Fonction qui retourne le code ASCII du caractère passé en entrée ou le caractère correspondant au code ascii en entrée
#Exemple
#Entrée: 'A'
#Sortie: 33
#Entrée: 33
#Sortie: A 
def quelleplace(ch):
    if type(ch)==str:
        if (len(ch) != 1):
            print("la chaine entrée n'est pas de la bonne taille (i.e : len = 1)")
            return
        x = ord(ch) - 32
    elif type(ch)==int:
        if (ch < 0 | ch > 95):
            print("l'entier entrée n'est pas inclut dans l'intervalle [0,95]")
            return 
        x=chr(ch+32)
    else:
        print("ch n'est pas du bon type")    
    return x 
    
#Fonction qui renvois le résultat de nb modulo 95
def modulo95(nb):
    return nb%95

#Fonction qui calcule l'inverse du déterminant d'une matrice en utilisant l'algorithme d'Euclide étendu
def inversedet(a,b):
    r, u, v, rr, uu, vv = a, 1, 0, b, 0, 1
    while rr:
        q = r // rr
        r, u, v, rr, uu, vv = rr, uu, vv, r - q * rr, u - q * uu, v - q * vv
    return u
#Fonction qui retourne le déterminant d'une matrice 
def getDet(a,b,c,d):
    return a*d - c*b
#Fonction qui calcule l'inverse d'une matrice et qui retourne la matrice inversée 
def inversematrix(a,b,c,d):
    listemat=[]#liste qui contiendra la matrice inversée
    #on initialise la matrice 
    a=a
    b=-b
    c=-c
    d=d
    #On calcule le déterminant inverse
    invdet=inversedet(getDet(a,b,c,d),95)
#Afin d'inversé la matrice on effectue le calcul : inverse du déterminant * Matrice , ce qui revient à multiplier chacun des composants de la matrice par l'inverse du déterminant
    a= invdet*a
    b= invdet*b
    c= invdet*c
    d= invdet*d
#On ajoute les composants de la matrice dans la liste que l'on va retourner 
    listemat.append(d)
    listemat.append(b)
    listemat.append(c)
    listemat.append(a)
#On retourne la liste contenant la matrice inversée 
    return listemat

#Fonction pour coder un mot en utilisant le chiffre de Hill
#On considère ici que m=2 tout le temps 
def HillCode(mot,a,b,c,d):
    x=len(mot)# on stocke la taille du mot 
    #Si la longeur du message à chiffrer n'est pas pair on ajoute un espace
    if(len(mot)%2!=0):
        mot=mot+" "
    y= x/2 # divise la longueur du mot par 2 afin de pouvoir le parcourir 2 par 2 ( m=2 )
    lreconstruit=[]#Liste contenant le message chiffrer 
    
    ind2=0
    #On va ici effectuer les opérations suivantes:
    #On parcours le message 2 lettres par 2 lettres
    #On récupère la place de la lettre dans l'alphabet ( ici son code Ascii)
    #On multiplie ensuite chaque lettre par la matrice et on le stocke dans les variables y1,y2,.......,yn
    #On prends ensuite le modulo des différents y et on le stocke dans z1,z2,.....zn
    #On stocke les z dans la liste lreconstruit et on obtient notre message chiffrer
    for i in range (0,int(y)):
        x1=int(quelleplace(mot[ind2]))
        x2=int(quelleplace(mot[ind2+1]))
        ind2=ind2+2
        y1=x1*a + x2*b
        y2=x1*c + x2*d
        z1=modulo95(y1)
        z2=modulo95(y2)
        lreconstruit.append(quelleplace(z1))
        lreconstruit.append(quelleplace(z2))
    print(''.join(lreconstruit)) #On affiche le message chiffrer pour l'utilisateur 
        
#Fonction pour déchiffrer le message 
#On cherche l'inverse de la matrice 
#Une fois cela fait on applique les mêmes étapes que pour le chiffrement mais avec la matrice inverse 
def HillDcode(messagechiffrer,a,b,c,d):
    x=len(messagechiffrer)
    if(len(messagechiffrer)%2!=0):
        messagechiffrer=messagechiffrer+" "
    y= x/2
    lreconstruit=[]
    lmatinv=inversematrix(a,b,c,d)
    #Dans la fonction inversematrix la liste renvoyée est de la forme  [d,b,c,a] 
    #De ce fait lorsque l'on initialse les composantes de la matrice on ira donc chercher a à l'indice 3, b à l'indice 1 etc..
    a=lmatinv[3]
    b=lmatinv[1]
    c=lmatinv[2]
    d=lmatinv[0]
    ind2=0
    for i in range (0,int(y)):
        x1=int(quelleplace(messagechiffrer[ind2]))
        x2=int(quelleplace(messagechiffrer[ind2+1]))
        ind2=ind2+2
        y1=x1*d + x2*b
        y2=x1*c + x2*a
        z1=modulo95(y1)
        z2=modulo95(y2)
        lreconstruit.append(quelleplace(z1))
        lreconstruit.append(quelleplace(z2))
    print(''.join(lreconstruit))
    