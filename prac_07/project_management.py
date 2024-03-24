import datetime
from project import Project

MENU = """
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit
"""


def main():
    """main function to manage the project management system."""
    projects = load_projects()

    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        print(MENU)

        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_str = input("Enter date to filter projects (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == "A":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice. Please choose a valid option.")

        choice = input("Enter your choice: ").upper()

    save_choice = input("Would you like to save to projects.txt? (yes/no): ")
    if save_choice.lower() == "yes":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def load_projects():
    """load projects from the projects.txt file"""
    projects = []
    in_file = open('projects.txt', 'r')
    in_file.readline()
    for line in in_file:
        data = line.strip().split('\t')
        project = Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4]))
        projects.append(project)
    return projects


def save_projects(projects):
    """save projects to the projects.txt file"""
    out_file = open('projects.txt', 'w')
    for project in projects:
        out_file.write(
            f"{project.name} {project.start_date.strftime('%d/%m/%Y')} {project.priority} {project.cost_estimate} {project.completion_percentage}")
    out_file.close()
    print("Projects saved successfully.")


def display_projects(projects):
    """display all projects, sorted by completion."""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(project)


def filter_projects_by_date(projects, date_str):
    """filter projects by a specified date"""
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]

    print("Filtered projects:")
    for project in sorted(filtered_projects):
        print(project)


def add_new_project():
    """
    Add a new project to the list.
    """
    name = input("Enter project name: ")
    start_date = input("Enter start date (dd/mm/yyyy): ")
    priority = int(input("Enter priority: "))
    cost_estimate = float(input("Enter cost estimate: "))
    completion_percentage = int(input("Enter completion percentage: "))

    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """
    Update an existing project's completion percentage or priority.
    """
    print("Select a project to update:")
    for i, project in enumerate(projects):
        print(f"{i}: {project}")

    choice = int(input("Enter project number: "))
    selected_project = projects[choice]

    print("Selected project to update:")
    print(selected_project)

    new_completion = input("Enter new completion percentage : ")
    if new_completion != "":
        selected_project.completion_percentage = int(new_completion)

    new_priority = input("Enter new priority : ")
    if new_priority != "":
        selected_project.priority = int(new_priority)

    print("Project updated")


main()
