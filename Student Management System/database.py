students=[]

def add_student(new_student):
    students.append(new_student)
    
def remove_student(student_id):
    removed_student= None
    for student in students:
        if student['id'] == student_id:
            removed_student = student
            students.remove(student)
            break

    return removed_student   

def view_students():
    return students

def student_count():
    return len(students)

def search_student(student_id):
    searched_student= None
    for student in students:
        if student['id'] == student_id:
            searched_student = student
            break

    return searched_student