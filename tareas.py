# Gestor de Tareas en Python
def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")

def gestionar_tareas():
    tareas = []
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            if not tareas:
                print("\nNo hay tareas pendientes.")
            else:
                print("\nLista de tareas:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
                    
        elif opcion == "2":
            nueva_tarea = input("Escribe la nueva tarea: ").strip()
            if nueva_tarea:
                tareas.append(nueva_tarea)
                print(f"¡Tarea '{nueva_tarea}' agregada con éxito!")
            else:
                print("La tarea no puede estar vacía.")
                
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    gestionar_tareas()