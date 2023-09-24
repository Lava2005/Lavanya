class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  #sort the listof students in descending order of CGPA
  sorted_students=sorted(student_list,
                         key=lambda student:student.cgpa,reverse=True)
  return sorted_students

#Example usage
student=[Student("Lavanya","A123",8.6),
         Student("Arya","A124",8.9),
         Student("Mala","A125",9.1),
         Student("Dhana","A126",9.9),]

sorted_Students=sort_students(student)
#print the sorted list of students 
for student in sorted_Students:
  print("Name:{},Roll Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
  