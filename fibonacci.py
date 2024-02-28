def fibonacci(n):
    
    # Inicializando array
    fibonacci = [0, 1]
    
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    if n in fibonacci:
        return True
    else:
        return False

# Numero que vai ser analisado
numero = 5

result = fibonacci(numero)

if result:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

