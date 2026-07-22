students = []
FILE_NAME = "practice/projects/students.txt"

def save_students():
    file = open(FILE_NAME,"w")
    for student in students:
        line = str(student["roll_no"])+","+str(student["Name"])+","+str(student["Mark"])+"\n"
        file.write(line)
    file.close()

def load_students():
    try:
        file = open(FILE_NAME,"r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            parts=line.split(",")
            student={"roll_no":int(parts[0]),"Name":parts[1],"Mark":float(parts[2])}
            students.append(student)
        file.close()
    except FileNotFoundError:
        return
    
def find_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None

def display_student(student):
    print("=" * 30)
    print(f"Roll No : {student['roll_no']}")
    print(f"Name    : {student['Name']}")
    print(f"Mark    : {student['Mark']}")
    print("=" * 30)

def add_student():
    roll_no = int(input("Enter the roll_no: "))
    while roll_no<=0:
        print("Roll number must be greater than zero")
        roll_no = int(input("Enter the roll_no: "))
    for i in students:
        if i["roll_no"] == roll_no:
            print("Roll number already exists")
            break
    else:
        name = input("Enter name: ")
        mark = float(input("Enter mark: "))
        while mark > 100 or mark <0:
            print("Enter a valid mark")
            mark = float(input("Enter mark: "))
        student={"roll_no":roll_no,"Name":name,"Mark":mark}
        students.append(student)
        print("\nStudent added successfully.\n")
        save_students()

def view_student():
    if len(students) == 0:
        print("No students found.")
    else:
        print("------------------")
        for student in students:
            # for detail in student:
            #     print(detail ," : ",student[detail])
            # print("------------")
            display_student(student)

def search_student():
    print("\n1.Search by roll no \n2.Search by name\n")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            search_roll = int(input("Enter the roll no: "))
            for student in students:
                if(student["roll_no"] == search_roll):
                    # for detail in student:
                    #     print(detail ," : ",student[detail])
                    display_student(student)
                    break
            else:
                print("Student not found.")
        elif choice == 2:
            search_name = input("Enter the name: ")
            for student in students:
                if student["Name"] == search_name:
                    # for details in student:
                    #     print(details ,":",student[details])
                    display_student(student)
                    break
            else:
                print("Student not found")
    except ValueError:
        print("Enter a valid choice")

def update_student():
    update_roll = int(input("Enter the roll no of the student that you want to update: "))
    for student in students:
        if student["roll_no"] == update_roll:
            update_mark = float(input("Enter the updated mark: "))
            while update_mark > 100 or update_mark <0:
                print("Enter a valid mark")
                update_mark = float(input("Enter mark: "))
            student["Mark"] = update_mark
            print("Updation successful")
            save_students()
            break
    else:
        print("Student not found")

def delete_student():
    delete_roll = int(input("Enter the roll no of the student that you want to delete: "))
    student = find_student(delete_roll)
    if student:
            students.remove(student)
            print("Student removed successfullyy")
            save_students()
    else:
        print("Student not fount")

def average_mark():
    total = 0
    count = 0
    if len(students) == 0:
        print("No students available")
        return
    for student in students:
        total += student["Mark"]
        count += 1
    average_mark = total/count
    print("The average mark : ",average_mark)

def statistics():
    print("\n1.Total Students \n2.Highest Mark\n3.Lowest Mark\n4.Pass Percentage\n5.Fail Percentage")
    try: 
       choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter the valid choice")
    if choice == 1:
        total = 0
        for student in students:
            total += 1
        print("Total students = ",total)
    elif choice == 2:
        largest = 0
        for student in students:
            if student["Mark"] > largest:
                largest= student["Mark"]
        print("The Highest mark = ",largest)
    elif choice == 3:
        lowest = 101
        for student in students:
            if student["Mark"]<lowest:
                lowest=student["Mark"]
        print("The Lowest mark = ",lowest)
    elif choice == 4:
        pass_mark = 60
        total = 0
        passed_students = 0
        if len(students)== 0:
            print("No students avilable")
            return
        for i in students:
            total += 1
            if i["Mark"]>=pass_mark:
                passed_students +=1
        pass_percentage = (passed_students/total)*100
        print("Pass Percentage: ",pass_percentage)
    elif choice == 5:
        pass_mark = 60
        failed = 0
        total = 0
        for i in students:
            total += 1
            if i["Mark"]<pass_mark:
               failed +=1
        fail_percentage = (failed/total)*100
        print("Fail Percentage: ",fail_percentage)
    elif choice<1 or choice > 5:
        print("Enter a valid choice")

def grades():
    if len(students) == 0:
      print("No students available")
      return
    for student in students:
        if student["Mark"] >= 90:
            print(student["Name"],":","A")
        elif student["Mark"] >= 80 and student["Mark"]<90:
            print(student["Name"],":","B")
        elif student["Mark"] >= 70 and student["Mark"]<80:
            print(student["Name"],":","C")
        elif student["Mark"] >= 60 and student["Mark"]<70:
            print(student["Name"],":","D")
        elif student["Mark"] <60:
            print(student["Name"],":","F")

def sort_students():
    print("\n1. By Roll Number\n2. By Marks\n3. By Name")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        students.sort(key = lambda student:student["roll_no"])
    elif choice == 2:
        students.sort(key=lambda student:student["Mark"])
    elif choice == 3:
        students.sort(key = lambda student: student["Name"].lower())
    elif choice >3:
        print("Invalid choice")
        return
    print("\nSorted Students :\n")
    for student in students:
            # print("---------------------------")
            # print("Roll no :",student["roll_no"])
            # print("Name    :",student["Name"])
            # print("Mark    :",student["Mark"])
         display_student(student)


def main_menu():
    choice = 0
    while choice != 10:
        print("1.Add student \n2.View student \n3.Search student \n4.Update Student \n5.Delete student \n6.Average marks \n7.Statistics \n8.Grades \n9.Sort students \n10.Exit")
        try:
           choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a number")
            continue
        if choice == 1:
            add_student()
        elif choice == 2:
            view_student()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            average_mark()
        elif choice == 7:
            statistics()
        elif choice == 8:
            grades()
        elif choice == 9:
            sort_students()
        elif choice<1 or choice>10:
            print("Enter a valid choice")

load_students()
main_menu()