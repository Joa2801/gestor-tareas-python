import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tareas import cargar_tareas, guardar_tareas, agregar_tarea, completar_tarea, eliminar_tarea
from rich.console import Console
from rich.table import Table

class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.console = Console()
        
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        
        ttk.Label(self.frame, text="Título:").grid(row=0, column=0, sticky=tk.W)
        self.titulo_entry = ttk.Entry(self.frame, width=30)
        self.titulo_entry.grid(row=0, column=1)
        
        ttk.Label(self.frame, text="Descripción:").grid(row=1, column=0, sticky=tk.W)
        self.Descripción_entry = ttk.Entry(self.frame, width=30)
        self.Descripción_entry.grid(row=1, column=1)
        
        ttk.Label(self.frame, text="Prioridad:").grid(row=2, column=0, sticky=tk.W)
        self.prioridad_combo = ttk.Combobox(self.frame, values=["alta", "media", "baja"])
        self.prioridad_combo.grid(row=2, column=1)
        
        
        ttk.Button(self.frame, text="Agregar", command=self.agregar).grid(row=3, column=0, pady=5)
        ttk.Button(self.frame, text="Mostrar en Rich", command=self.mostrar_rich).grid(row=3, column=1)
        ttk.Button(self.frame, text="Marcar como completada", command=self.marcar_completada).grid(row=4, column=0)
        ttk.Button(self.frame, text="Eliminar tarea", command=self.eliminar).grid(row=4, column=1)
        ttk.Button(self.frame, text="Salir", command=self.salir).grid(row=5, column=0, columnspan=2, pady=10)

    def agregar(self):
        titulo = self.titulo_entry.get()
        Descripción = self.Descripción_entry.get()
        prioridad = self.prioridad_combo.get()
        
        if titulo and prioridad:
            tareas = cargar_tareas()
            agregar_tarea(tareas, titulo, Descripción, prioridad)
            guardar_tareas(tareas)
            self.titulo_entry.delete(0, tk.END)
            self.Descripción_entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", "Tarea agregada")
        else:
            messagebox.showerror("Error", "Título y prioridad son obligatorios")

    def marcar_completada(self):
        tareas = cargar_tareas()
        if not tareas:
            messagebox.showwarning("Advertencia", "No hay tareas para marcar")
            return
            
        id_tarea = simpledialog.askinteger("Marcar como completada", "Ingrese el ID de la tarea a marcar:")
        if id_tarea is not None:
            if completar_tarea(tareas, id_tarea):
                guardar_tareas(tareas)
                messagebox.showinfo("Éxito", f"Tarea {id_tarea} marcada como completada")
            else:
                messagebox.showerror("Error", f"No se encontró la tarea con ID {id_tarea}")

    def eliminar(self):
        tareas = cargar_tareas()
        if not tareas:
            messagebox.showwarning("Advertencia", "No hay tareas para eliminar")
            return
            
        id_tarea = simpledialog.askinteger("Eliminar tarea", "Ingrese el ID de la tarea a eliminar:")
        if id_tarea is not None:
            if eliminar_tarea(tareas, id_tarea):
                guardar_tareas(tareas)
                messagebox.showinfo("Éxito", f"Tarea {id_tarea} eliminada")
            else:
                messagebox.showerror("Error", f"No se encontró la tarea con ID {id_tarea}")

    def mostrar_rich(self):
        tareas = cargar_tareas()
        if not tareas:
            messagebox.showinfo("Información", "No hay tareas para mostrar")
            return
            
        table = Table(title="Tareas", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="cyan")
        table.add_column("Título", style="green")
        table.add_column("Descripción", style="white")
        table.add_column("Prioridad", style="yellow")
        table.add_column("Estado", style="blue")
        
        for tarea in tareas:
            estado = "✓" if tarea.get("estado") == "completada" else "●"
            table.add_row(
                str(tarea["id"]),
                tarea["título"],
                tarea.get("descripción", ""),
                tarea["prioridad"],
                estado
            )
        
        self.console.print(table)

    def salir(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()