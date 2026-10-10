"""Gestor básico para las prácticas de colaboración."""


def agregar_tarea(tareas: list[dict], titulo: str) -> dict:
    """Agrega una tarea pendiente y devuelve la nueva tarea."""
    if not titulo.strip():
        raise ValueError("El título no puede estar vacío")
    nuevo_id = max((t["id"] for t in tareas), default=0) + 1
    tarea = {"id": nuevo_id, "titulo": titulo.strip(), "completada": False}
    tareas.append(tarea)
    return tarea


def listar_tareas(tareas: list[dict]) -> list[dict]:
    """Devuelve las tareas sin modificar la lista original."""
    return list(tareas)
