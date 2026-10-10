import unittest

from tareas.gestor import agregar_tarea, listar_tareas


class GestorTests(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        nueva = agregar_tarea(tareas, "  Ejercicio Git  ")
        self.assertEqual(nueva["titulo"], "Ejercicio Git")
        self.assertEqual(nueva["id"], 1)
        self.assertFalse(nueva["completada"])

    def test_listar_tareas(self):
        tareas = []
        agregar_tarea(tareas, "Primera")
        self.assertEqual(len(listar_tareas(tareas)), 1)


if __name__ == "__main__":
    unittest.main()
