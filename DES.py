#Module pour chiffrer/déchiffrer un message en utilisant le DES

import base64





# Tables de permutation / expension
IP = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)
FP = (
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
)
PC1 = (
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
)
PC2 = (
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)

P = (
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11, 4,  25
)

E  = (
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)
 
# Nombre de rotation (subkeys)
Nrot = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)

# S-boxes
Sboxes = {
    0: (
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
    ),
    1: (
        15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
        3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9 
    ),
    2: (
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
        1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 
    ),
    3: (
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
    ),
    4: (
        2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
        4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
    ),
    5: (
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
    ),
    6: (
        4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
        13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
    ),
    7: (
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
        1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
        7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
        2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
    )
}
# ENTREE : Un bloc binaire (int2), une table de permutation
# SORTIE : Le bloc binaire permuté (int2)
def permutation(block,block_length, perm_table):


    block_str = (bin(block)[2:]).zfill(block_length)

    # Permutation du bloc
    perm_block = []
    for ind_char in range(len(perm_table)):
        perm_block.append(block_str[perm_table[ind_char]-1])

    # Retourner le bloc permuté
    return int(''.join(perm_block),2)

# ENTREE : Un bloc binaire (int2) de taille 56
# SORTIE : Le bloc décalé à gauche de k bits (int(2))
def left_rotation(block, k):


    # Découpage 28 | 28
    left_block = (block >> 28)
    right_block = (block & 0xFFFFFFF)

    # Décalage à gauche (On fait attention ici lorsqu'un bit dépasse la borne gauche, qu'il soit remis à droite)
    rot_l = lambda b, k=1: ((b<<k)|(b>>(28-k)))&((1<<28)-1)
    left_block = (bin(rot_l(left_block,k))[2:]).zfill(28)
    right_block = (bin(rot_l(right_block,k))[2:]).zfill(28)

    block_complete = int((left_block+right_block),2)

    return block_complete

# Fonction qui calcule et retourne la liste des 16 sous-clés (48 bits)
# ENTREE : Cle binaire 64 bits (str), k_rot décalage binaire
# SORTIE : Dictionnaire des 16 sous-clés de 48 bits (str)
def subkeys(cle):
   

    # Permutation PC1 de la cle (64bits -> 56bits)
    cle_pc1 = permutation(cle,64, PC1)
    # Dictionnaire qui va contenir les 16 sous-clés
    subkey_dict = dict.fromkeys(range(0,16))
    # Calcul des 16 sous-clés

    for cle_x in subkey_dict.keys():
        # Rotation à gauche
        cle_pc1 = left_rotation(cle_pc1, Nrot[cle_x])
        # Permutation PC2
        subkey_dict[cle_x] = permutation(cle_pc1,56,PC2)
    return subkey_dict

# ENTREE : bloc de droite du message 32bits (int2), sous-clés de 48bits correspondant à l'itération en cours
# SORTIE : Bloc de 32 bits (int2)
def feistel_fct (block_R, subkey):


    # Expension du bloc R
    block_R_exp = permutation(block_R,32,E)

    # block_R_exp (OU-EXCLUSIF) subkey
    block_48 = block_R_exp^subkey
    block_48_str = (bin(block_48)[2:]).zfill(48)
    # Découpage pour les S-BOXES
    blocks_IN_SBOXES = list((block_48_str[0+i:6+i] for i in range(0, len(block_48_str), 6)))


    # Passage des 6 blocs dans les S-Boxes
    blocks_OUT_SBOXES = [] # list str
    for ind_box, block_in in enumerate(blocks_IN_SBOXES):
        # Pour avoir la ligne et la colonne de l'entier à récupérer dans le tableau Sbox courant
        # On utilise le masque block_in et des décalages à droites
        row = (((0b100000 & int(block_in,2)) >> 4) + (0b1 & int(block_in, 2)))
        col = (0b011110 & int(block_in,2)) >> 1
    
        blocks_OUT_SBOXES.append((bin(Sboxes[ind_box][16*row+col])[2:]).zfill(4))

    # Permutation P
    block_IN_P = int((''.join(blocks_OUT_SBOXES)),2)
    block_OUT_P = permutation(block_IN_P,32,P)
    return block_OUT_P

# Fonction permettant d'effectuer le chiffrement DES
# ENTREE : message binaire , cle
# SORTIE : message binaire codé/décodé
def DESCode(message,cle,decode=False):


    # Vérification
    if (len(message) > 64):
        print("Le message est supérieur à 64 bits")
        return

    if (len(cle) > 64):
        print("La clé donnée pour le DES est trop grande")
        return
    elif (len(cle) < 64):
        print("La clé donnée pour le DES est trop petite")
        return

    #Vérifier la binarité du message et de la clé
    msg_check = int(message,2)
    cle_check = int(cle, 2)


    # Dictionnaire des 16 sous-clés
    subkey_dict = subkeys(cle_check)
    print("\nDictionnaire des sous-clés : \n"+str(subkey_dict))

    # Permutation initiale
    msg_IP = permutation(msg_check,64,IP)
    print("\nPERMUTATION INITIALE IP = "+(bin(msg_IP)[2:]).zfill(64))
    # L0 / R0
    L0 = msg_IP >> 32
    R0 = msg_IP & 0xFFFFFFFF # Utilisation d'un masque pour garder uniquement les 32 derniers bits.
    
    # 16 rounds
    last_L = L0
    last_R = R0
    print("\nL0 = "+bin(L0))
    print("R0 = "+bin(R0))
    for i in range (1,17):
        
        #Dans le cas où l'on décode, on utile les clés dans le sens inverse
        if (decode):
            i = 17-i

        Li = last_R
        Ri = last_L^feistel_fct(last_R,subkey_dict[i-1])
        last_L = Li
        last_R = Ri
        print("\nL"+str(i)+" = "+(bin(Li)[2:]).zfill(32)) #Ri-1 
        print("R"+str(i)+" = "+(bin(Ri)[2:]).zfill(32)) #Li-1 (+) f(Ri-1)

    # Concaténation
    last_L_str = (bin(last_L)[2:]).zfill(32)
    last_R_str = (bin(last_R)[2:]).zfill(32)

    msg_after_rounds = int(last_R_str+last_L_str,2)

    # Permutation finale
    final_msg = permutation(msg_after_rounds,64,FP)
    print("\nPERMUTATION FINALE FP = "+(bin(final_msg)[2:]).zfill(64)+"\n")

    return final_msg

    
#code = bin(DESCode("0000000100100011010001010110011110001001101010111100110111101111", '0001001100110100010101110111100110011011101111001101111111110001'))
#code = hex(DESCode("0000000100100011010001010110011110001001101010111100110111101111", '0001001100110100010101110111100110011011101111001101111111110001'))
