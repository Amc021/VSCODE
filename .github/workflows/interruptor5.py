def descobrir_interruptores():
    # Inicialmente, todos os interruptores estão desligados
    interruptores = [False, False, False]

# Ligue o primeiro interruptor e espere um tempo
    interruptores[0] = True
    # Simula a espera para a lâmpada esquentar
    tempo_espera()

# Ligue o segundo interruptor e vá para a sala das lâmpadas
    interruptores[1] = True
    # Vá para a sala das lâmpadas
    lampadas = verificar_lampadas(interruptores)

# Identifique as lâmpadas
    if lampadas[0] == 'quente':
        lampada1 = 0
    elif lampadas[0] == 'acesa':
        lampada1 = 1
    else:
        lampada1 = 2

# Desligue o segundo interruptor e ligue o terceiro
    interruptores[1] = False
    interruptores[2] = True
    # Vá para a sala das lâmpadas novamente
    lampadas = verificar_lampadas(interruptores)

# Identifique as outras lâmpadas
    if lampadas[1] == 'quente':
        lampada2 = 0
    elif lampadas[1] == 'acesa':
        lampada2 = 1
    else:
        lampada2 = 2

    lampada3 = 3 - lampada1 - lampada2

    return lampada1, lampada2, lampada3

def tempo_espera():
    import time
    time.sleep(5)  # Simula a espera de 5 segundos

def verificar_lampadas(interruptores):
    lampadas = []
    for i in range(3):
        if interruptores[i]:
            lampadas.append('acesa')
        else:
            lampadas.append('apagada')
    return lampadas

# Teste a função
print(descobrir_interruptores())