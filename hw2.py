students_list = []
students_dict = {}

students_list.append("Karma Dema")
students_dict["Karma Dema"] = "18"
students_dict["Karma Dema"] = "12"

students_list.append("Dechen")
students_dict["Dechen"] = "19"
students_dict["Dechen"] = "12"

students_list.append("Tashi")
students_dict["Tashi"] = "17"
students_dict["Tashi"] = "11"

search_title = input("Enter student's name: ")
x = input("Enter student's age: ")
y = input("Enter student's grade: ")
if search_title in students_list:
    print(f"Student information added successfully!") 
else:
    print("not found!")
print("List of students:")  
for student in students_list:
    print(student)


