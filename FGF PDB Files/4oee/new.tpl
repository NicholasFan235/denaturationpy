### This is a temporary parameter file made for residue IDY ###
### Make sure that all the parameters are verified before using this file as a global parameter file ###

CONFLIST IDY        IDYBK 

NATOM    IDYBK      18

IATOM    IDYBK  S      0
IATOM    IDYBK  C1     1
IATOM    IDYBK  O1     2
IATOM    IDYBK  C2     3
IATOM    IDYBK  O2     4
IATOM    IDYBK  C3     5
IATOM    IDYBK  O3     6
IATOM    IDYBK  C4     7
IATOM    IDYBK  O4     8
IATOM    IDYBK  C5     9
IATOM    IDYBK  O5    10
IATOM    IDYBK  C6    11
IATOM    IDYBK  C7    12
IATOM    IDYBK  O6A   13
IATOM    IDYBK  O6B   14
IATOM    IDYBK  OS1   15
IATOM    IDYBK  OS2   16
IATOM    IDYBK  OS3   17

ATOMNAME IDYBK    0  S  
ATOMNAME IDYBK    1  C1 
ATOMNAME IDYBK    2  O1 
ATOMNAME IDYBK    3  C2 
ATOMNAME IDYBK    4  O2 
ATOMNAME IDYBK    5  C3 
ATOMNAME IDYBK    6  O3 
ATOMNAME IDYBK    7  C4 
ATOMNAME IDYBK    8  O4 
ATOMNAME IDYBK    9  C5 
ATOMNAME IDYBK   10  O5 
ATOMNAME IDYBK   11  C6 
ATOMNAME IDYBK   12  C7 
ATOMNAME IDYBK   13  O6A
ATOMNAME IDYBK   14  O6B
ATOMNAME IDYBK   15  OS1
ATOMNAME IDYBK   16  OS2
ATOMNAME IDYBK   17  OS3

CONNECT  IDYBK  S   ion        0    O2   0    OS1  0    OS2  0    OS3
CONNECT  IDYBK  C1  ion        0    O1   0    C2   0    O5 
CONNECT  IDYBK  O1  ion        0    C1   0    C7 
CONNECT  IDYBK  C2  ion        0    C1   0    O2   0    C3 
CONNECT  IDYBK  O2  ion        0    S    0    C2 
CONNECT  IDYBK  C3  ion        0    C2   0    O3   0    C4 
CONNECT  IDYBK  O3  ion        0    C3 
CONNECT  IDYBK  C4  ion        0    C3   0    O4   0    C5 
CONNECT  IDYBK  O4  ion        0    C4 
CONNECT  IDYBK  C5  ion        0    C4   0    O5   0    C6 
CONNECT  IDYBK  O5  ion        0    C1   0    C5 
CONNECT  IDYBK  C6  ion        0    C5   0    O6A  0    O6B
CONNECT  IDYBK  C7  ion        0    O1 
CONNECT  IDYBK  O6A ion        0    C6 
CONNECT  IDYBK  O6B ion        0    C6 
CONNECT  IDYBK  OS1 ion        0    S  
CONNECT  IDYBK  OS2 ion        0    S  
CONNECT  IDYBK  OS3 ion        0    S  

### This is a temporary parameter file made for residue GNX ###
### Make sure that all the parameters are verified before using this file as a global parameter file ###

CONFLIST GNX        GNXBK 

NATOM    GNXBK      19

IATOM    GNXBK  N2     0
IATOM    GNXBK  C1     1
IATOM    GNXBK  S1     2
IATOM    GNXBK  C2     3
IATOM    GNXBK  C3     4
IATOM    GNXBK  O3     5
IATOM    GNXBK  C4     6
IATOM    GNXBK  O4     7
IATOM    GNXBK  C5     8
IATOM    GNXBK  O5     9
IATOM    GNXBK  C6    10
IATOM    GNXBK  O6    11
IATOM    GNXBK  O12   12
IATOM    GNXBK  S12   13
IATOM    GNXBK  O1S   14
IATOM    GNXBK  O22   15
IATOM    GNXBK  O2S   16
IATOM    GNXBK  O32   17
IATOM    GNXBK  O3S   18

ATOMNAME GNXBK    0  N2 
ATOMNAME GNXBK    1  C1 
ATOMNAME GNXBK    2  S1 
ATOMNAME GNXBK    3  C2 
ATOMNAME GNXBK    4  C3 
ATOMNAME GNXBK    5  O3 
ATOMNAME GNXBK    6  C4 
ATOMNAME GNXBK    7  O4 
ATOMNAME GNXBK    8  C5 
ATOMNAME GNXBK    9  O5 
ATOMNAME GNXBK   10  C6 
ATOMNAME GNXBK   11  O6 
ATOMNAME GNXBK   12  O12
ATOMNAME GNXBK   13  S12
ATOMNAME GNXBK   14  O1S
ATOMNAME GNXBK   15  O22
ATOMNAME GNXBK   16  O2S
ATOMNAME GNXBK   17  O32
ATOMNAME GNXBK   18  O3S

CONNECT  GNXBK  N2  ion        0    S1   0    C2 
CONNECT  GNXBK  C1  ion        0    C2   0    O5 
CONNECT  GNXBK  S1  ion        0    N2   0    O1S  0    O2S  0    O3S
CONNECT  GNXBK  C2  ion        0    N2   0    C1   0    C3 
CONNECT  GNXBK  C3  ion        0    C2   0    O3   0    C4 
CONNECT  GNXBK  O3  ion        0    C3   0    S12
CONNECT  GNXBK  C4  ion        0    C3   0    O4   0    C5 
CONNECT  GNXBK  O4  ion        0    C4 
CONNECT  GNXBK  C5  ion        0    C4   0    O5   0    C6 
CONNECT  GNXBK  O5  ion        0    C1   0    C5 
CONNECT  GNXBK  C6  ion        0    C5   0    O6 
CONNECT  GNXBK  O6  ion        0    C6 
CONNECT  GNXBK  O12 ion        0    S12
CONNECT  GNXBK  S12 ion        0    O3   0    O12  0    O22  0    O32
CONNECT  GNXBK  O1S ion        0    S1 
CONNECT  GNXBK  O22 ion        0    S12
CONNECT  GNXBK  O2S ion        0    S1 
CONNECT  GNXBK  O32 ion        0    S12
CONNECT  GNXBK  O3S ion        0    S1 

