
import pickle
from enum import Enum
import os
import pydoc

# TODO 1: Implement error handling for user input
# Add code to validate and handle user input errors. For example, when prompting for a number, make sure the input is a valid integer.

# TODO 2: Implement the ability to delete a student from the list
# Extend the delete_student() function to include the option of deleting a student by their name and ID. Update the user interface to accommodate this feature.

# TODO 3: Implement additional options submenu
# Create a new function, additional_options(), which will present users with additional actions they can perform, such as updating test grades or deleting specific tests.

# TODO 4: Implement saving data and exiting the program
# Add code to the save_and_exit() function to ensure that the data is saved before exiting the program. Provide proper user feedback and handle any potential errors.


# Enum for different actions in the menu
class Actions(Enum):
    ADD_STUDENT = 1
    SHOW_STUDENTS = 2
    ADD_GRADE = 3
    SHOW_GRADES = 4   
    SHOW_AVERAGE = 5
    DELETE_STUDENT = 6 
    EXIT = 0

# Class representing a test
class Test:
    def __init__(self, name_test, grade):
        self.name = name_test
        self.grade = grade

# Class representing a student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.test_list = []

    def __str__(self):
        return f"Student: {self.name}  ID: {self.student_id}"
      
    def add_test(self, test_type, grade):
        self.test_list.append(Test(test_type, grade))

students = []  # List to store student records

# The main menu function that provides options and handles user input
def menu():
    while True:
        print_actions()
        user_selection = get_user_selection()
        if user_selection == Actions.ADD_STUDENT:
            clear_terminal()
            add_student()   
        elif user_selection == Actions.SHOW_STUDENTS:
            clear_terminal()
            show_students()
            
        elif user_selection == Actions.ADD_GRADE:
            clear_terminal()  
            add_grade()
        elif user_selection == Actions.SHOW_GRADES:
            clear_terminal() 
            show_grades()
        elif user_selection == Actions.SHOW_AVERAGE:
            clear_terminal() 
            show_average()
        elif user_selection == Actions.DELETE_STUDENT:
            clear_terminal() 
            delete_student()   
        elif user_selection == Actions.EXIT:
            save_and_exit()
            clear_terminal()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
# Print the available menu actions
def print_actions():
    print("Available actions:")
    for action in Actions:
        print(f'{action.name} = {action.value}')

# Get the user's menu selection
def get_user_selection():
    return Actions(int(input("Enter your selection:")))

# Add a new student to the list
def add_student():
    load_from_pickle()  
    name = input("Enter name:")
    student_id = input("Enter id:")
    students.append(Student(name, student_id))
    print(f'{name} id: {student_id} added to students')
    save_to_pickle()

# Display the list of students
def show_students():
    load_from_pickle()
    for student in students:
        print(f'{student.name} id: {student.student_id}')

# Add a test grade for a student
def add_grade():
    student = search()
    if student:
        test_type = input("Enter test:")
        grade = input("Enter grade:")
        student.add_test(test_type, grade)
        print(f'{test_type}={grade} was added')
        save_to_pickle()
    else:
        print("Student not found.")

# Display test grades for a student
def show_grades():
    student = search()
    if student:
        for test in student.test_list:
            print(f'{student.name} id: {student.student_id} test {test.name} grade {test.grade}')
    else:
        print("Student not found.")

# Calculate and display the average grade for a student
def show_average():
    student = search()
    if student:
        total_sum = sum(int(test.grade) for test in student.test_list)
        average = total_sum / len(student.test_list)
        print(f'{student.name} id: {student.student_id} average grade {average}')
    else:
        print("Student not found.")

# Delete a student from the list
def delete_student():
    name = input("Enter student's name to delete:")
    student_id = input("Enter student's id to delete:")
    students[:] = [student for student in students if student.name != name and student.student_id != student_id]
    save_to_pickle()
    print(f'Student {name} id : {student_id} is deleted')

# Search for a student by name
def search():
    load_from_pickle()  
    name_to_search = input("Enter student's name:")
    for student in students:
        if name_to_search == student.name:
            return student
    return None

# Save student data to pickle file
def save_to_pickle():
    try:
        with open('students.pickle', 'wb') as binary_save:
            pickle.dump(students, binary_save)
            print('Data saved to students.pickle')
    except Exception as e:
        print('Error saving data:', e)      

# Load student data from pickle file
def load_from_pickle():
    try:
        with open('students.pickle', "rb") as binary_load:
            global students
            students = pickle.load(binary_load)
            print('Data loaded from students.pickle')  
    except FileNotFoundError:
        print('students.pickle not found, starting with an empty list')

# Save data and exit the program
def save_and_exit():
    save_to_pickle()
    print("Thank you and goodbye")
    exit()




if __name__ == "__main__":
    menu()
    





if __name__ == "__main__":
    menu()
   

