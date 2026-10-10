# NEXOM Knowledge Hub — Escenario 2: colaboración mediante fork

Proyecto de práctica para **Fork → Clone → Branch → Commit → Push → Pull Request → Review → Merge → Sync fork → Pull**.

## Cómo ejecutar

Requiere Python 3.10 o superior. Desde la raíz del proyecto:

```bash
python main.py
python -m unittest discover -s tests -v
```

En algunos equipos, el comando de Python es `python3` o `py`.

## Punto de partida

El proyecto ya permite agregar y listar tareas. Las mejoras **no vienen resueltas**: cada desarrollador las implementará en su fork.

- **Desarrollador A:** implementar `completar_tarea(tareas, id_tarea)` en `tareas/gestor.py`; al encontrar el ID, poner `completada=True` y devolver `True`; devolver `False` cuando no exista. Agregar pruebas.
- **Desarrollador B:** implementar `buscar_tareas(tareas, texto)` en `tareas/busqueda.py`, con búsqueda por título sin distinguir mayúsculas/minúsculas, sin modificar la lista. Agregar pruebas.

**Instructor:** crear el repositorio público `nexom-git-fork` en GitHub, subir este código base a `main` y mantenerlo como repositorio original. Cada desarrollador hará fork hacia su cuenta personal. No dar permisos de escritura sobre el original durante este escenario.

Consulta `ejercicios/GUIA_ESCENARIO_2.md` para el recorrido completo de la demostración y su verificación.
