##########################
#MODULE PRINCIPAL
#Contient l'interface terminal et représente l'application elle même
#########################


import sys
import Hill
import Transposition
import Vigenere
import DES


if len(sys.argv) < 2:
    
    print("++++++++++++++++++++++++++++++++++++\n             CryptoPy !\n++++++++++++++++++++++++++++++++++++\n\n Bienvenue sur l'application CryptoPY ! \n\n CryptoPy est une application implémentant plusieurs algorithme de chiffrement / déchiffrement tel que : \n\t-Le chiffre de césar\n\t-Le chiffre de Hill\n\t-La transposition rectangulaire\n\t-Le DES\n\t-Le chiffrement de Vigenère\nSi vous ne savez pas comment utiliser l'application veuillez consulter le manuel avec la commande --help\n++++++++++++++++++++++++++++++++++++")
else:    
    ## Chiffrement de Cesar
    if sys.argv[1] == "-cesar":
        if sys.argv[2] == "-c":
            print("entrez la cle")
            cle=input()
            print("entrez le texte en clair")
            txt=input()
            list=[]
            for i in txt:
                i= ord(i)+cle
                list.append(chr(i))
            print(" voici le message chiffrer : ")
            print(''.join(list))
        if sys.argv[2] == "-d":
            print("entrez la cle")
            cle=input()
            print("entrez le message coder")
            txt=input()
            list=[]
            for i in txt:
                i= ord(i)-cle
                list.append(chr(i))
            print("voici le message :")
            print(''.join(list))
    #Manuel
    if sys.argv[1] == "--help":
        print("-------------------------------------------\n")
        print("-------------        MANUEL     -----------\n") 
        print("-------------------------------------------\n")
        print("-----------  1.Liste commandes  -----------\n")
        print("-  [-nom du chiffrement] [-c]:pour coder\n")
        print("-  [-nom du chiffrement] [-d]:pour dcoder\n")
        print("----------- 2.Chiffrements dispo ----------\n")
        print("- [-cesar]:cesar                      \n") 
        print("- [-Hill]:Hill                        \n")      
        print("- [-transpose]:transposition rectangulaire          \n")     
        print("- [-DES]:DES                          \n")
        print("- [-Vigenere]:Vigenere                          \n")
    #Chiffre de Hill
    if sys.argv[1] == "-Hill":
        if sys.argv[2] == "-c":
            print("entrez a")
            a=input()
            print("entrez b")
            b=input()
            print("entrez c")
            c=input()
            print("entrez d")
            d=input()
            print("entrez le texte en clair")
            txt=input()
            print(" voici le message chiffrer : ")
            Hill.HillCode(txt,int(a),int(b),int(c),int(d))
        if sys.argv[2] == "-d":
            print("entrez le message coder")
            txt=input()
            print("entrez a")
            a=input()
            print("entrez b")
            b=input()
            print("entrez c")
            c=input()
            print("entrez d")
            d=input()
            print("\n")
            print("voici le message :")
            Hill.HillDcode(txt,int(a),int(b),int(c),int(d))
    #Transposition rectangulaire
    if sys.argv[1] == "-Transpo":
        if sys.argv[2] == "-c":
            print("entrez clef : ")
            a=input()
            print("entrez message : ")
            b=input()
            print("\n")
            print("voici le carre ainsi que le message chiffrer: \n")
            Transposition.AfficheCarre(Transposition.carre(a,b))
            print("\n")
            Transposition.chiffreTranspo(Transposition.carre(a,b))
        if sys.argv[2] == "-d":
            print("entrez la clef")
            clef=input()
            print("entrez le message chiffer")
            mess=input()
            print("\n")
            print("voici le carre ainsi que le message dechiffer: \n")
            Transposition.dechiffre(clef,mess) 
    if sys.argv[1] == "-Vigenere":
        if sys.argv[2] == "-c":
            print("entrez la clef : ")
            a=input()
            print("entrez le message : ")
            b=input()
            print("\n")
            print("voici le message chiffrer:")
            print(Vigenere.VIGCode(b,a,decode=False))
            print("\n")
        if sys.argv[2] == "-d":
            print("entrez la clef")
            clef=input()
            print("entrez le message chiffer")
            mess=input()
            print("\n")
            print("voici le message dechiffer:")
            print(Vigenere.VIGCode(mess,clef,decode=True))
    
    if sys.argv[1] == "-DES":
        if sys.argv[2] == "-c":
            print("entrez la clef (64bits): ")
            a=input()
            print("entrez le message : ")
            b=input()
            print("\n")
            print("voici le message chiffrer en binaire:")
            print(bin(DES.DESCode(b,a,decode=False)))
            print("\n")
            print("voici le message chiffrer en hexadécimal")
            print(hex(DES.DESCode(b,a,decode=False)))
            print("\n")
        if sys.argv[2] == "-d":
            print("entrez la clef")
            clef=input()
            print("entrez le message chiffer")
            mess=input()
            print("\n")
            print("voici le message dechiffer en binaire:")
            print(bin(DES.DESCode(mess,clef,decode=True)))
            print("\n")
            print("voici le message dechiffer en hexadécimal:")
            print(hex(DES.DESCode(mess,clef,decode=True)))
    

