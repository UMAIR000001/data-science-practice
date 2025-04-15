# ************Mid_Exam of OOPS  Long Question*****************

# Define a class named 'course'
class course:
    
    # Class-level list to store enrolled students (shared across all instances)
    list_of_enroll_students = []
    
    # Constructor method to initialize course name
    def __init__(self, course_name):
        self.course_name = course_name
    
    # Method to enroll a student to the course
    def enroll(self, student_name):
        # Append student name to the class-level list
        updated_list = self.list_of_enroll_students.append(student_name)
        return updated_list  # returns None, as append doesn't return anything useful
    
    # Method to remove a student from the course
    def remove(self, student_name):
        # Remove student name from the class-level list
        updated_list = self.list_of_enroll_students.remove(student_name)
        return updated_list  # returns None, as remove doesn't return anything

# Create first course object and enroll a student
obj1 = course("OOPS")
obj1.enroll("Umair")  # Enroll "Umair" in the course

# Create second course object and enroll another student
obj2 = course("OOPS")
obj2.enroll("Umair baloch")  # Enroll "Umair baloch"

# Remove "Umair" using obj1
obj1.remove("Umair")  # Remove "Umair" from the class-level list

# Print the list of enrolled students (shared among all objects)
print(course.list_of_enroll_students)  # Output: ['Umair baloch']
