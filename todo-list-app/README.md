# Todo List App

Este proyecto es una aplicación de lista de tareas que permite a los usuarios gestionar sus tareas de manera eficiente. La aplicación está implementada en Python y proporciona varias funcionalidades para añadir, listar, editar, completar y eliminar tareas.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `todo_list.py`: Implementación de la aplicación de lista de tareas. Define la clase `Task` con los atributos `id`, `description`, `status` y `creation_date`. Incluye funciones para gestionar las tareas:
  - `add_task(description)`: Añade una nueva tarea.
  - `list_tasks()`: Lista todas las tareas.
  - `mark_task_complete(task_id)`: Marca una tarea como completada.
  - `clear_all_tasks()`: Limpia toda la lista de tareas.
  - `edit_task(task_id, new_description)`: Edita una tarea existente.
  - `delete_task(task_id)`: Elimina una tarea específica.

- `requirements.txt`: Lista las dependencias necesarias para el proyecto.

## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, simplemente corre el archivo `todo_list.py` en tu entorno de Python. Puedes interactuar con la aplicación a través de la consola.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un issue o un pull request.