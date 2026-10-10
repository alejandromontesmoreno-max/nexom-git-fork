from tareas.gestor import listar_tareas, agregar_tarea


def main():
    tareas = []
    agregar_tarea(tareas, "Preparar capacitación Git")
    agregar_tarea(tareas, "Revisar Pull Requests")
    print("GESTOR DE TAREAS NEXOM")
    for tarea in listar_tareas(tareas):
        estado = "✓" if tarea["completada"] else "·"
        print(f"{estado} [{tarea['id']}] {tarea['titulo']}")


if __name__ == "__main__":
    main()
