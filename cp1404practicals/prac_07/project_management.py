from project import load_projects, save_projects, display_projects, filter_projects_by_date, add_new_project, \
    update_project


def display_menu():
    menu = "Menu:\n" \
           "(L)oad projects\n" \
           "(S)ave projects\n" \
           "(D)isplay projects\n" \
           "(F)ilter projects by date\n" \
           "(A)dd new project\n" \
           "(U)pdate project\n" \
           "(Q)uit"
    print(menu)


def main():
    file_name = 'projects.txt'
    projects = load_projects(file_name)

    while True:
        display_menu()
        option = input(">>> ").lower()

        if option == 'l':
            file = input("Enter filename to load projects from: ")
            projects = load_projects(file) if file else projects
        elif option == 's':
            file = input("Enter filename to save projects to: ")
            save_projects(projects, file) if file else save_projects(projects, file_name)
        elif option == 'd':
            display_projects(projects)
        elif option == 'f':
            filter_projects_by_date(projects)
        elif option == 'a':
            add_new_project(projects)
        elif option == 'u':
            update_project(projects)
        elif option == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option. Please choose from the menu.")


if __name__ == '__main__':
    main()
