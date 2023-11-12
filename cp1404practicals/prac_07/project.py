import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def update_completion(self, percentage):
        self.completion = percentage if 0 <= percentage <= 100 else self.completion

    def update_priority(self, new_priority):
        self.priority = new_priority if new_priority > 0 else self.priority


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip the header
            for line in file:
                data = line.strip().split('\t')
                name, start_date, priority, estimate, completion = data
                project = Project(name, start_date, int(priority), float(estimate), int(completion))
                projects.append(project)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return projects


def save_projects(projects, file_name):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete = [project for project in projects if project.completion < 100]
    completed = [project for project in projects if project.completion == 100]
    incomplete_sorted = sorted(incomplete, key=lambda x: x.priority)
    completed_sorted = sorted(completed, key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_sorted:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_sorted:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_sorted = sorted(filtered_projects, key=lambda x: x.start_date)

    for project in filtered_sorted:
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, estimate, completion)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            new_percentage = int(input("New Percentage: "))
            new_priority = int(input("New Priority: ") or project.priority)
            project.update_completion(new_percentage)
            project.update_priority(new_priority)
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input.")


