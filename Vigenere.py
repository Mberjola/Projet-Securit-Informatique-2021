#Module pour chiffrer/déchiffrer un message en utilisant le chiffrement de Vigenère



#Fonction qui renvois le résultat de nb modulo 95
def modulo95(nb):
    return nb%95

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

# Fonction dont le rôle est de construire une chaine de la même longueur que le message
# à partir de la clé
def construct_str_key(len_msg, key):
    if len_msg <= len(key):
        return key[:len_msg]
    else:
        key_str = key
        for i in range(len_msg - len(key)):
            key_str += key[i % len(key)]
        return key_str


# Fonction pour chiffrer/dechiffrer un message
def VIGCode(message, key, decode=False):
    
    len_msg = len(message) # Longueur du message à coder

    crypted_text = "" # Message codé
    key_txt = construct_str_key(len_msg, key) # Chaine construite avec la clé
    
    for i in range(len_msg):
        
        char_msg = message[i] # caractère courant du message à coder
        char_key = key_txt[i] # caractère courant de la chaine key_txt

        # Cas ou l'on decode (soustraction de position char_key)
        if (decode):
            int_cryp_char = modulo95(quelleplace(char_msg) - quelleplace(char_key))

        # Cas ou l'on code (addition de position char_key)
        else :
            int_cryp_char = modulo95(quelleplace(char_msg) + quelleplace(char_key))
        cryp_char = quelleplace(int_cryp_char)

        # Ajout du caractère décodé/codé dans la chaine qui sera retourner
        crypted_text += cryp_char

    return crypted_text






