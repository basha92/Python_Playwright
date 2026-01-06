#this file has student details module inside StudentPackage
def get_student_details(student_id):
    # In a real application, this might fetch details from a database
    student_database = {
        1: {"name": "Alice", "age": 20, "course": "Computer Science"},
        2: {"name": "Bob", "age": 22, "course": "Mechanical Engineering"},
        3: {"name": "Charlie", "age": 21, "course": "Mathematics"},
    }
    return student_database.get(student_id, "Student not found")