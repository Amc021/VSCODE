def contarletraa(s):
    """Conta quantas vezes a letra 'a' (minúscula) aparece na string s."""
    return s.count('a')

def contarletraA(s):
    """Conta quantas vezes a letra 'A' (maiúscula) aparece na string s."""
    return s.count('A')

def main():
    # Solicita a string ao usuário
    entrada = input("Digite uma string para verificar a letra 'a' e 'A': ")

    # Conta as ocorrências das letras 'a' e 'A'
    quantidade_a = contarletraa(entrada)
    quantidade_A = contarletraA(entrada)

    # Exibe os resultados
    print(f"A letra 'a' (minúscula) aparece {quantidade_a} vez(es) na string.")
    print(f"A letra 'A' (maiúscula) aparece {quantidade_A} vez(es) na string.")

if __name__ == "__main__":
    main()