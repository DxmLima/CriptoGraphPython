def dracarys (frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + "01000001 01100110 01110010 01101001 01100011 01100001 \n"
        if letra in "Bb":
            tradutor = tradutor + "01000010 01101001 01101100 01101100 01101001 01100101 00100000 01001010 01100101 01100001 01101110 00001010 \n"
        if letra in "Cc":
            tradutor = tradutor + "01000011 01100001 01110010 01100101 01101100 01100101 01110011 01110011 00100000 01010111 01101000 01101001 01110011 01110000 01100101 01110010 \n "
        if letra in "Dd":
            tradutor = tradutor + "01000100 01101111 01101110 00100111 01110100 00100000 01010011 01110100 01101111 01110000 00100000 01000010 01100101 01101100 01101001 01100101 01110110 01101001 01101110 00100111 \n "
        if letra in "Ee":
            tradutor = tradutor + "01000101 01110110 01100101 01110010 01111001 00100000 01000010 01110010 01100101 01100001 01110100 01101000 00100000 01011001 01101111 01110101 00100000 01010100 01100001 01101011 01100101 \n "
        if letra in "Ff":
            tradutor = tradutor + "01000110 01101111 01110010 01100101 01110110 01100101 01110010 00100000 01011001 01101111 01110101 01101110 01100111 \n "
        if letra in "Gg":
            tradutor = tradutor + "01000111 01101001 01110010 01101100 01110011 00100000 01001010 01110101 01110011 01110100 00100000 01010111 01100001 01101110 01110100 00100000 01110100 01101111 00100000 01001000 01100001 01110110 01100101 00100000 01000110 01110101 01101110 \n "
        if letra in "Hh":
            tradutor = tradutor + "01001000 01101111 01101100 01100100 01101001 01101110 01100111 00100000 01001111 01110101 01110100 00100000 01100110 01101111 01110010 00100000 01100001 00100000 01001000 01100101 01110010 01101111 \n"
        if letra in "Ii":
            tradutor = tradutor + "01001100 01101001 01101011 01100101 00100000 01100001 00100000 01010110 01101001 01110010 01100111 01101001 01101110 00001010\n "
        if letra in "Jj":
            tradutor = tradutor + "01001010 01100101 01110011 01110011 01101001 01100101 00100111 01110011 00100000 01000111 01101001 01110010 01101100 \n"
        if letra in "Kk":
            tradutor = tradutor + "01001011 01101001 01101100 01101100 01100101 01110010 00100000 01010001 01110101 01100101 01100101 01101110 \n"
        if letra in "Ll":
            tradutor = tradutor + "01001100 01101001 01110110 01101001 01101110 00100111 00100000 01001111 01101110 00100000 01100001 00100000 01010000 01110010 01100001 01111001 01100101 01110010 \n"
        if letra in "Mm":
            tradutor = tradutor + "01001101 01100001 01101110 01101001 01100001 01100011 \n "
        if letra in "Nn":
            tradutor = tradutor + "01001110 01100101 01110110 01100101 01110010 00100000 01000111 01101111 01101110 01101110 01100001 00100000 01000111 01101001 01110110 01100101 00100000 01011001 01101111 01110101 00100000 01010101 01110000 \n"
        if letra in "Oo":
            tradutor = tradutor + "01001111 01101110 01101100 01111001 00100000 01011001 01101111 01110101 \n"
        if letra in "Pp":
            tradutor = tradutor + "01010000 01101111 01110111 01100101 01110010 00100000 01101111 01100110 00100000 01001100 01101111 01110110 01100101 \n"
        if letra in "Qq":
            tradutor = tradutor + "01010001 01110101 01100101 01100101 01101110 00100000 01101111 01100110 00100000 01001000 01100101 01100001 01110010 01110100 01110011 \n"
        if letra in "Rr":
            tradutor = tradutor + "01010010 01110101 01101110 01101110 01101001 01101110 01100111 00100000 01010101 01110000 00100000 01010100 01101000 01100001 01110100 00100000 01001000 01101001 01101100 01101100 \n"
        if letra in "Ss":
            tradutor = tradutor + "01010011 01101000 01101111 01110101 01101100 01100100 00100000 01001001 00100000 01010011 01110100 01100001 01111001 00100000 01101111 01110010 00100000 01010011 01101000 01101111 01110101 01101100 01100100 00100000 01001001 00100000 01000111 01101111 \n"
        if letra in "Tt":
            tradutor = tradutor + "01010100 01101001 01101101 01100101 00100000 01000001 01100110 01110100 01100101 01110010 00100000 01010100 01101001 01101101 01100101 \n"
        if letra in "Uu":
            tradutor = tradutor + "01010101 01101110 01100100 01100101 01110010 00100000 01010000 01110010 01100101 01110011 01110011 01110101 01110010 01100101 \n"
        if letra in "Vv":
            tradutor = tradutor + "01010110 01101111 01100111 01110101 01100101 00001010 \n"
        if letra in "Xx":
            tradutor = tradutor + "01011000 01100001 01101110 01100001 01100100 01110101 00001010 \n"
        if letra in "Yy":
            tradutor = tradutor + "01011001 01101111 01110101 00100000 01000111 01101001 01110110 01100101 00100000 01001100 01101111 01110110 01100101 00100000 01100001 00100000 01000010 01100001 01100100 00100000 01001110 01100001 01101101 01100101 \n"
        if letra in "Zz":
            tradutor = tradutor + "01011010 01101001 01100111 01100111 01111001 00100000 01010011 01110100 01100001 01110010 01100100 01110101 01110011 01110100 \n "

    return tradutor

print(dracarys(input('Digite algo')))