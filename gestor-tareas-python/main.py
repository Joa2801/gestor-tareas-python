from tareas import cargar_tareas, guardar_tareas, agregar_tarea, mostrar_tareas
from rich import print

def main():
    tareas = cargar_tareas()
    
    while True:
        print("\n[bold]--- GESTOR DE TAREAS ---[/bold]")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Ver todas las tareas")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            titulo = input("Título de la tarea: ")
            Descripción = input("Descripción: ")
            prioridad = input("Prioridad (alta/media/baja): ").lower()
            agregar_tarea(tareas, titulo, Descripción, prioridad)
            
        
            
        elif opcion == "4":
            mostrar_tareas(tareas)
            
        elif opcion == "5":
            guardar_tareas(tareas)
            print("[green]¡Tareas guardadas! Hasta pronto.[/green]")
            break
            
        else:
            print("[red]Opción no válida. Intente nuevamente.[/red]")

if __name__ == "__main__":
    main()