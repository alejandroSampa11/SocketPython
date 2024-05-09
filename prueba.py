def hamming_codificacion(data):
    m = len(data)
    r=0
    while 2**r<m+r+1:
        r+=1
    
    datos_codificados = [0]*(m+r)
    j=0
    k=0

    for i in range(1,m+r+1):
        if i ==2**k:
            datos_codificados[i-1] = 0
            k+=1
        else:
            datos_codificados[i-1]=int(data[j])
            j+=1
    
    for i in range(r):
        paridad = 0
        for j in range(2**i-1,m+r,2**(i+1)):
            for k in range(2**i):
                if j+k<m+r:
                    paridad ^= datos_codificados[j+k]
        datos_codificados[2**i-1]=paridad
    
    return datos_codificados

def hamming_decodificacion(encoded_data):
    r = 0
    while 2**r < len(encoded_data) + 1:
        r += 1

    error_position = 0
    syndrome = 0

    for i in range(r):
        parity = 0
        for j in range(2**i - 1, len(encoded_data), 2**(i + 1)):
            for k in range(2**i):
                if j + k < len(encoded_data):
                    parity ^= encoded_data[j + k]
        syndrome += parity * (2**i)

    if syndrome != 0:
        error_position = syndrome

    if error_position > 0:
        # Corregir el error
        encoded_data[error_position - 1] ^= 1
        print("HUBO UN ERROR EN LA POSICION ", error_position-1)

    # REMOVER LOS BITS DE PARIDAD PARA OBTENER LOS DATOS ORIGINALES
    decoded_data = []
    for i in range(len(encoded_data)):
        if i + 1 != 2**r:
            decoded_data.append(encoded_data[i])

    return decoded_data


# texto = input("Ingrese un texto: ")

# bits_ascii = [format(ord(char), '08b') for char in texto]

# bits_concatenados = ''.join(bits_ascii)
bits_concatenados = "1101"
print("BITS ",bits_concatenados)
codificado = hamming_codificacion(bits_concatenados)
print("Encoded data:", codificado)
decoded_data = hamming_decodificacion(codificado)
print("Decoded data:", decoded_data)