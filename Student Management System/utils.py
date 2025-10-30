import database


def show_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")


def format_student(student):
    return f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}"


def perform_operation(choice):

    if choice == "1":
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        new_student = {"id": id, "name": name, "age": age}
        database.add_student(new_student)
        print("Student added successfully.")

    elif choice == "2":
        students = database.view_students()
        if len(students) == 0:
            print("No students found.")
        else:
            print(format(" Student List ", "*^40"))
            for student in students:
                print(format_student(student))
            print("*" * 50)

    elif choice == "3":
        if database.student_count() == 0:
            print("No students to delete.")
        else:
            id = int(input("Enter Student ID to delete: "))
            removed_student = database.remove_student(id)
            print(f"Removed Student: {format_student(removed_student)}")

    elif choice == "4":
        if database.student_count() == 0:
            print("No students to search.")
        else:
            id = int(input("Enter Student ID to search: "))
            searched_student = database.search_student(id)
            if searched_student:
                print(f"Found Student: {format_student(searched_student)}")
            else:
                print("Student not found.")

    elif choice == "5":
        print("Exiting the system...")

    else:
        print("Invalid choice. Please try again.")
