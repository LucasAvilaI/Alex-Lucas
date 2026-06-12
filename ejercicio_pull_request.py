# Crear codigo basico para practicar cambios y pulls

nota = [1,2,3,4]

for x,y in enumerate(nota):
    print(x,y)

def media_notas(notas: list) -> float:
    """
    Recibe las notas en una lista.
    Calcula la media y devuelve el resultado en un float.
    """

    return sum(notas)/len(notas)

nota_media = media_notas(nota)

print(f"La media de las notas es: {nota_media}")