# utils/data_manager.py
import json

# Ruta al archivo JSON donde se almacenan los proyectos
FILE_PATH = 'data/projects_data.json'

# Obtener todos los proyectos
def get_all_projects():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar todos los proyectos
def save_all_projects(projects):
    with open(FILE_PATH, 'w') as file:
        json.dump(projects, file, indent=4)

# Agregar un nuevo proyecto
def add_project_data(name, investment_amount, estimated_return, duration_months):
    projects = get_all_projects()
    projects.append({
        "name": name,
        "investment_amount": investment_amount,
        "estimated_return": estimated_return,
        "duration_months": duration_months
    })
    save_all_projects(projects)

# Eliminar un proyecto
def delete_project_data(name):
    projects = get_all_projects()
    projects = [project for project in projects if project['name'] != name]
    save_all_projects(projects)
