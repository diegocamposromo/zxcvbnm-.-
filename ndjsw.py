class Resena:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

# Crear una lista vacía para almacenar las reseñas
resenas = []

# Función para agregar una reseña a la lista
def agregar_resena():
    titulo = input("Ingrese el título de la reseña: ")
    contenido = input("Ingrese el contenido de la reseña: ")
    resena = Resena(titulo, contenido)
    resenas.append(resena)
    print("Reseña agregada con éxito!")

# Función para mostrar todas las reseñas de la lista
def mostrar_resenas():
    if resenas:
        for i, resena in enumerate(resenas):
            print(f"Reseña {i+1}:")
            print(f"Título: {resena.titulo}")
            print(f"Contenido: {resena.contenido}")
            print("------------------------------")
    else:
        print("No hay reseñas para mostrar.")

# Ejecutar un bucle para mostrar un menú y realizar acciones
while True:
    print("1. Agregar una reseña")
    print("2. Mostrar todas las reseñas")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        agregar_resena()
    elif opcion == "2":
        mostrar_resenas()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")

print("¡Hasta luego!")