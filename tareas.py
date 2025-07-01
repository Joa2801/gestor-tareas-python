import json
import logging

logging.basicConfig(filename='registro.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def normalizar_tareas():
    tareas = cargar_tareas()
    for tarea in tareas:

        if "descripcion" in tarea:
            tarea["descripción"] = tarea.pop("descripcion")
        elif "Descripción" in tarea:
            tarea["descripción"] = tarea.pop("Descripción")
    guardar_tareas(tareas)




def cargar_tareas():
    try:
        with open("tareas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open("tareas.json", "w") as f:
        json.dump(tareas, f, indent=4)

def agregar_tarea(tareas, titulo, descripción, prioridad):
    nueva_tarea = {
        "id": len(tareas) + 1,
        "título": titulo,
        "descripción": descripción,  
        "prioridad": prioridad,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    logging.info(f"Tarea agregada: {titulo}")

def mostrar_tareas(tareas):
    from rich.table import Table
    table = Table(title="Listado de Tareas", show_header=True, header_style="bold blue")
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Título", style="magenta", min_width=20)
    table.add_column("Descripción", style="dim", min_width=30)
    table.add_column("Prioridad", style="green", width=10)
    table.add_column("Estado", style="red", width=8)
    
    for tarea in tareas:
        desc = tarea.get("descripción") or tarea.get("Descripción") or tarea.get("descripcion", "Sin descripción")
        estado = "✓" if tarea.get("estado") == "completada" else "●"
        
        table.add_row(
            str(tarea["id"]),
            tarea["título"],
            desc,  
            tarea["prioridad"].capitalize(),
            estado
        )
    print(table)
    
def completar_tarea(tareas, id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["estado"] = "completada"
            guardar_tareas(tareas)
            logging.info(f"Tarea completada: ID {id_tarea}")
            return True
    return False

def eliminar_tarea(tareas, id_tarea):
    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_tarea:
            tareas.pop(i)
            guardar_tareas(tareas)
            logging.info(f"Tarea eliminada: ID {id_tarea}")
            return True
    return False

def mostrar_tareas(tareas):
    from rich.table import Table
    table = Table(title="Listado de Tareas", show_header=True, header_style="bold blue")
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Título", style="magenta", min_width=20)
    table.add_column("Descripción", style="dim", min_width=30) 
    table.add_column("Prioridad", style="green", width=10)
    table.add_column("Estado", style="red", width=8)
    
    for tarea in tareas:
        estado = "✓" if tarea.get("estado") == "completada" else "●"
        prioridad = tarea["prioridad"].capitalize()
        
        table.add_row(
            str(tarea["id"]),
            tarea["título"],
            tarea.get("descripción", "Sin descripción"),  
            prioridad,
            estado
        )
    print(table)
    
    
    
    for tarea in tareas:
        if 'descripcion' in tarea:
            tarea['descripción'] = tarea.pop('descripcion')
            modificado = True
            
        if 'Descripción' in tarea:
            tarea['descripción'] = tarea.pop('Descripción')
            modificado = True
    
    if modificado:
        guardar_tareas(tareas)
        logging.info("Descripciones normalizadas a formato con tilde")
        return True
    return False