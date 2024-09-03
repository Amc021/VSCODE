def next_element(sequence):
    if sequence == 'a':
        # Sequência de números ímpares
        return [1, 3, 5, 7, 9]
    elif sequence == 'b':
        # Sequência de potências de 2
        return [2, 4, 8, 16, 32, 64, 128]
    elif sequence == 'c':
        # Sequência de quadrados perfeitos
        return [0, 1, 4, 9, 16, 25, 36, 49]
    elif sequence == 'd':
        # Sequência de quadrados de números pares
        return [4, 16, 36, 64, 100]
    elif sequence == 'e':
        # Sequência de Fibonacci
        return [1, 1, 2, 3, 5, 8, 13]
    elif sequence == 'f':
        # Sequência específica
        return [2, 10, 12, 16, 17, 18, 19, 20]
    else:
        return "Sequência não reconhecida"

# Testando a função
print(next_element('a'))
print(next_element('b'))
print(next_element('c'))
print(next_element('d'))
print(next_element('e'))
print(next_element('f'))