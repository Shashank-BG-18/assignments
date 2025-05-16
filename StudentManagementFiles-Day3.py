class Student:
    def __init__(self,id,name,course,avg_marks):
        self.id=id          #defining the data members
        self.name=name
        self.course=course
        self.avg_marks=avg_marks
    
    def __str__(self):
        return f"ID : {self.id} , Name : {self.name} , Course : {self.course} , Avgerage Marks : {self.avg_marks}"

class StudentManagement:
    def __init__(self):
        self.students={}    #creating of dictionary data member

    def add_student(self,student):   #Passing the student object
        self.students[student.id]=student
        print("\nStudent added successfully")

    def display(self):      #Display the data
        if not self.students:
            print("No students available to display")
        else:
            for student in self.students.values():
                print(student)
    
    def update_student_detail(self,id,name=None,course=None,avg_marks=None):    #Update the student details except id
        if id in self.students:
            if name:
                self.students[id].name=name
            if course:
                self.students[id].course=course
            if avg_marks:
                self.students[id].avg_marks=avg_marks
            print("Student details updated successfully")
        else:
            print("Student record not found to update")

    def delete_student_record(self,id): #delete the student record
        if id in self.students:
            del self.students[id]
            print("Student record deleted successfully")
        else:
            print("Student record not found")

def main():
    s=StudentManagement()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display student info")
        print("3.Update student record")
        print("4.Delete student record")
        print("5. Exit")

        choice=input("Enter your choice : ")

        if choice=='1':
            id=input("Enter student id : ")
            name=input("Enter the student name : ")
            course=input("Enter the student's course : ")
            avg_marks=input("ENter the student's average marks : ")
            student = Student(id,name,course,avg_marks)
            s.add_student(student)

        elif choice=='2':
            s.display()
        
        elif choice=='3':
            id=input("Enter student id to be updated : ")
            name=input("Enter the updated student name (else skip by pressing enter): ")
            course=input("Enter the updated student's course (else skip by pressing enter) : ")
            avg_marks=input("Enter the updated student's average marks (else skip by pressing enter) : ")
            name=name
            course=course
            avg_marks=avg_marks
            s.update_student_detail(id,name,course,avg_marks)

        elif choice=='4':
            id=input("Enter the student id to be deleted : ")
            s.delete_student_record(id)
        
        elif choice=='5':
            print("Thank You, Now will exit the program")
            break

        else:
            print("Invalid Choice, Please chose the correct option ")

if __name__=="__main__":
    main()



        
