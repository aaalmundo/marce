from collections import Counter

def caracteres_mas_repetidos_acumulado(contador):
    max_frecuencia = max(contador.values())
    caracteres = [caracter for caracter, frecuencia in contador.items() if frecuencia == max_frecuencia]
    return (caracteres, max_frecuencia)

contador_acumulado = Counter()

for _ in range(10):
    entrada_usuario = input("Ingrese un string: ")
    
    contador_acumulado.update(entrada_usuario)

    resultado = caracteres_mas_repetidos_acumulado(contador_acumulado)
    
    caracteres = "', '".join(resultado[0])  # Unir los caracteres en un string
    print(f"Los caracteres más repetidos hasta ahora son '{caracteres}' y se repiten {resultado[1]} veces.")

