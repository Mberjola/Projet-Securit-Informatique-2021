#Module pour chiffrer/déchiffrer un message en utilisant la transposition rectangulaire

import Hill
import math



#######Fonction utiles##############
#division euclidienne de a par b 
def divEuclidienne(a,b):
    resultat = a//b
    reste= a%b
    return resultat
#Retourne le reste de la division euclidienne de a par b 
def RestDivEuclid(a,b):
    resultat = a//b
    reste= a%b
    return reste
#Retourne une liste contenant des tuples  (clé trier dans l'ordre alphabétique , indice dans la clef )
#Exemple:
#Entrée : CHAT
#Sortie : [(2,A),(0,C),(1,H),(3,T)]
def ordreAlpha(clef):
    for i in clef:
        ordreAlpha = sorted((lettre, index) for index, lettre in enumerate(clef))
    return ordreAlpha

#Fonction qui enlève les espaces si le mot en comprends
#On récupère le message dans une liste, on enlève donc les espaces afin de ne pas se retrouver avec des indices du tableau contenant des espaces et non des lettres du message
#Entrée: TO TO 
#Sortie: ['T','O','T','T','O']
def enleveEspace(message):
    mess=[]
    for l in message:
        if l==" ":
            pass
        else:
            mess.append(l)
    return mess


#Fonction qui construit un carre à partir de la clef et du message 
#Exemple
#Entrée : clef : PAUL, message : SALUT
#Sortie:
#P A U L 
#S A L U
#T
def carre(clef,message):
    #initialisation des listes qui contiendront la clef, le message et le carré 
    listclef=[]
    listpos=[]
    listcarre=[]
    #On récupère la longeur du message 
    x= len(message)
    y= math.ceil(x/len(clef))
    #On stocke la clef dans la liste listclef
    for i in clef:
        listclef.append(i)
    #On ajoute la cle au carré 
    listcarre.append(listclef)
    #On va remplir le carré avec le message en prenant soin de ne pas dépasser la longueur de la clé : Ex : 
    #B I B M A T H
    #J E S U I S E
    #N I T A L I E  
    #A V E C M A R
    #I A 

    
    ind=0
    #Pour remplir le carre il faut d'abord parcourir pour 0 jusqu'à  (longueur du message / par le clé) .
    for k in range(int(y)):
        listremp=[] # liste temporaire qui va stocker les portions tu message à mettre dans le carre , on doit la vider à chaque passage dans la boucle for afin de ne pas se retrouver avec deux portions qui se superposent dans le carre
        while ind < x:
            if(message[ind]==" "): #Le message peut contenir des espaces, on ne les prends pas en compte 
                pass
            elif (len(listremp)<len(clef)): # Tant qu'on ne dépasse pas la taille de la clé on ajoute la portion à la liste temporaire
                listremp.append(message[ind])
            else:
                break #Si c'est le cas on sort de la boucle 
           
            ind = ind+1
        listcarre.append(listremp) #Et on ajoute la portion du message au carre
    return listcarre#On retourne la liste qui contient le carré construit 

#Fonction qui permet d'afficher le carré dans la console 
def AfficheCarre(listcarre):
    for i in listcarre:
        print(*i,sep =' ')
 

#On va maintenant chiffrer le message -> Correspond à l'étape où on classe les lettre de la clé dans l'ordre alphabétique et on réécrit chaque colonne 
#Dans l'ordre ex : 
#   #G R A I N      A G I N R       
    #S A L U T ==>  L S U T A
    #L E S P E      S L P E E
    #T I T S        T T S   I

def chiffreTranspo(listecarre):
    res=[]
    ordre = ordreAlpha(listecarre[0]) # On appelle la fonction ordreAlpha qui range les lettre par ordre alphabétique en conservant leurs index dans le mot initial
    #Ex : (C:0 H:1 :A:2 T:3) -> (A:2,C:0,H:1,T:3) -> le résultat est renvoyé sous forme de tuple on aura donc [(A,2),(C,0),....]
    for j,k in ordre:
        for l in range(1,len(listecarre)):
            if k < len(listecarre[l]):
                res.append(listecarre[l][k])
            else:
                pass
    print(" ".join(res))


        
#Fonction pour déchiffrer le mot obtenu
##La procédure 
###On reconstruit le tableau : nombre de ligne et nombre de colonnes
###Pour ce faire : On prends le longueur du message et on effectue la division euclidienne entre entre la longeur du message et la longueur de la clé
##Soit L la longueur de la clé, m la longueur du message et r le reste de la vision si il y en a on aura : m = L* a +r 
##On a donc maintenant le nombre de colonnes L tels que r colonnes ont une taille de a+1 et les colonnes restantes auront une taille de a
### ON répète ensuite les même étapes que pour le chiffrement afin de déchiffrer le mot 
def dechiffre(clef, message):
    ordre = ordreAlpha(clef) #On range les lettres de la clé par ordre alphabétique en conservant leurs indices dans le mot initial
    message = enleveEspace(message)#Le message peut contenir des espaces, on prends soin de les supprimer afin d'éviter de confondre un espace et un caractère lors du parsing 
    nbLettreDerniereCol=divEuclidienne(len(message),len(clef)) # on définit ici la taille des dernières colonnes
    nbLettre=nbLettreDerniereCol+1#taille des r colonnes
    restDiv= RestDivEuclid(len(message),len(clef)) #On stocke ici le reste de la division euclidienne afin de pouvoir faire la distinction entre les r colonnes et les dernières colonnes 
    res=[]# Liste qui contiendra les colonnes mais dans l'ordre établit par la fonction ordreAlpha
    messdechiffre=[]#Liste qui contiendra le message déchiffrer 
    
    
    #Pour chaque lettre dans l'ordre alphabétique on va récupérer r caractères tant que cela est possible, si l'indice de la lettre présent dans le tuple généré par OrdreAlpha
    #est plus grand que le reste de la division cela signifie qu'il appartient au groupe des dernières colonnes on le remplit donc de a caractères sinon on remplit les colonnes de a+1 caractères
    #tant que l'on a pas atteins la fin du message 
    ind=0
    for i,j in ordre:
        listetemp=[]#Définition de la liste temporaire qui va stocker les colonnes une a une ( une colonne maximum dans la liste à chaque passage )
        while(ind < len(message)):
            if(j<restDiv):
                if(len(listetemp) < nbLettre):
                    listetemp.append(message[ind])
                else:
                    break
            else:
                if(len(listetemp) < nbLettreDerniereCol):
                    listetemp.append(message[ind])
                else:
                    break

            ind=ind+1
        res.append((listetemp))
#On a maintenant obtenu les colonnes séparément, il s'agit désormais de les remettre dans l'ordre originial de la clef exemple:  
# pour CHAT -> On a  (A,C,H,T) et on veut obtenir : (C,H,A,T) avec C,H,A,T les colonnes du tableau
    ordre = enumerate(ordre)
    ordre = sorted(ordre, key=lambda tup: tup[1][1]) #On remet la clef dans le bon ordre en triant selon leurs emplacement dans la clef ex : C prends la position 0, H 2 etc..

    
    
#On re parcours désormais la liste contenant les colonnes mais dans le bon ordre
    for nb in range(math.ceil(len(message)/len(clef))): # Pour chaque ligne
        for x,y in ordre: # Pour chaque colonne
            if nb < len(res[x]):
                messdechiffre.append(res[x][nb])
    
        
    
    messdechiffre=[item for sublist in messdechiffre for item in sublist] #On transforme la liste de liste en une seule liste 
    AfficheCarre(carre(clef,messdechiffre)) # On affiche le carré obtenu 
    print("\n")
    print(" ".join(messdechiffre)) #On affiche le message déchiffrer
  


    

    



  
