# Guía de instructor — Escenario 2: Fork y Pull Request

## Objetivo

Mostrar cómo dos colaboradores sin permisos de escritura proponen modificaciones a un repositorio original mediante forks personales y Pull Requests.

## Preparación previa (instructor)

1. Crear `nexom-git-fork` en la cuenta de GitHub seleccionada. Elegir **Public** (o repositorio privado si la organización permite forks privados). Si el proyecto local ya tiene README y .gitignore, crear el remoto **vacío**.
2. Descomprimir el ZIP en una carpeta local, abrirla en VS Code, ejecutar `python main.py` y `python -m unittest discover -s tests -v`.
3. Inicializar Git desde **Source Control → Initialize Repository** o `git init`.
4. Preparar los archivos, confirmar con mensaje `chore: crear proyecto base` y publicar la rama `main` en GitHub. Si usa terminal: `git branch -M main`, `git remote add origin URL_DEL_ORIGINAL`, `git push -u origin main`.
5. Pedir que cada participante use su cuenta personal de GitHub. Verificar que NO tengan permisos de escritura sobre el original. En repositorios privados, comprobar de antemano la disponibilidad de forks.
6. Antes de comenzar, identificar qué participante será A (completar tareas) y B (buscar tareas).

## Demostración en orden

### 1. Fork — en GitHub

Cada participante abre el repositorio original y pulsa **Fork → Create fork**. Confirmar que se creó `USUARIO/nexom-git-fork` en **su propia cuenta**.

**Verificar:** ahora existen tres repositorios GitHub distintos: el original y dos forks personales.

### 2. Clone — desde VS Code

En VS Code: **Ctrl/Cmd+Shift+P → Git: Clone**, pegar la URL del fork personal y elegir carpeta de destino. Abrir la carpeta clonada.

Comando equivalente: `git clone URL_DEL_FORK`.

**Verificar:** `git remote -v` muestra `origin` apuntando al fork personal, NO al original.

### 3. Crear rama — desde VS Code

Crear una rama a partir de `main` usando el selector de rama de VS Code.

- A: `feature/completar-tarea`
- B: `feature/buscar-tareas`

Equivalente: `git switch -c feature/NOMBRE`.

**Verificar:** el indicador de rama de VS Code no dice `main`.

### 4. Desarrollo y commit — en el fork local

**Desarrollador A:** crear `completar_tarea(tareas, id_tarea)` dentro de `tareas/gestor.py` y agregar pruebas para un ID existente y otro inexistente.

**Desarrollador B:** crear `tareas/busqueda.py` con `buscar_tareas(tareas, texto)` y agregar pruebas para mayúsculas/minúsculas y coincidencias no existentes.

Ejecutar `python -m unittest discover -s tests -v`.

Desde Source Control: seleccionar **Stage Changes**, escribir mensaje y **Commit**.

- A: `feat: permitir completar tareas`
- B: `feat: agregar busqueda de tareas`

Comandos equivalentes: `git add .` y `git commit -m "feat: ..."`.

**Verificar:** hay un commit nuevo en la rama de cada participante.

### 5. Publicar rama — push al fork

Desde VS Code: **Publish Branch** o **Push**. Equivalente: `git push -u origin feature/NOMBRE`.

**Verificar:** la rama existe en `USUARIO/nexom-git-fork`, no en el repositorio original.

### 6. Pull Request — fork hacia el original

En GitHub, desde el fork, abrir **Compare & pull request** (o ir a Pull requests → New pull request). Confirmar:

- **base repository:** repositorio original (del instructor)
- **base:** `main`
- **head repository:** fork del participante
- **compare:** su rama `feature/...`

Crear el PR con descripción: qué cambia, pruebas ejecutadas y evidencia.

**Verificar:** el PR aparece en el repositorio original.

### 7. Revisión y merge — instructor

Abrir el PR, revisar **Files changed** y comentar una mejora. El participante hace el ajuste en su misma rama y vuelve a hacer `commit` y `push`; el PR se actualiza.

Cuando ambos PR hayan pasado las pruebas, el instructor los integra a `main` usando **Merge pull request**. Aprobar un PR y fusionarlo son pasos diferentes.

**Verificar:** la rama `main` del original contiene las dos funcionalidades.

### 8. Sync fork — GitHub de cada colaborador

En la página principal del fork personal, elegir `main` → **Sync fork → Update branch** (si GitHub ofrece ese flujo). Si hay conflictos o no aparece la opción, sincronizar mediante el remoto `upstream`.

**Verificar:** la rama `main` del fork personal tiene los commits integrados en el original.

### 9. Pull — VS Code de cada colaborador

En VS Code, cambiar a la rama **main** y usar **Pull** (o `git pull origin main`). Esto actualiza el clon local desde **su fork ya sincronizado**.

**Verificar:** en la copia local están las funciones de A y B.

## Precisión importante sobre Sync fork

Sync fork actualiza una rama del fork remoto, no todas las ramas del clon local. Cambiar primero a `main` y ejecutar **Pull** para traer a local la versión ya integrada. Las ramas `feature/...` no cambian automáticamente.

## Alternativa con remoto upstream (solo si hace falta)

```bash
git remote add upstream URL_DEL_ORIGINAL
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main
```

Los participantes deben estar en `main` limpia y sin modificaciones pendientes. Si el avance de `main` no es fast-forward, analizar la divergencia antes de integrar.

## Preguntas para cerrar

1. ¿Por qué `origin` apunta al fork y no al repositorio original?
2. ¿En qué repositorio aparece el Pull Request?
3. ¿Cuál es la diferencia entre aprobar un Pull Request y hacer merge?
4. ¿Por qué después de Sync fork todavía hace falta Pull en el equipo local?
5. ¿Qué cambió en `main` y qué pasó con las ramas `feature/`?

## Nota de seguridad

Usar datos ficticios, no publicar credenciales o tokens, y verificar que `.venv/` y `.env` estén excluidos por `.gitignore`.
