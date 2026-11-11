import csv

def load_students(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        student_list = []

        for line in reader:
            student_list.append(line)
        return student_list

def show_student(students, name_of_student):
    student_info = []

    for line in students:
        if line["name"].lower() == name_of_student.lower():
            student_info.append(line)
    return student_info

def add_student(students, new_name, new_surname, new_subject, new_mark):

    new_student = {
        "name": new_name,
        "surname": new_surname,
        "subject": new_subject,
        "mark": new_mark, 
    }
    students.append(new_student)
        
def save_students(filename, students):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "surname", "subject", "mark"])
        writer.writeheader()
        writer.writerows(students)

def highest_mark(students, subject):
    highest_mark = 0
    name_of_student = ""
    found_subject = False

    for line in students:
        if line["subject"].lower() == subject.lower():
            found_subject = True
            if int(line["mark"]) > highest_mark:
                highest_mark = int(line["mark"])
                name_of_student = line["name"]
    if found_subject:
        return highest_mark, name_of_student
    else:
        return None   

def average_grade(students, subject):
    total = 0
    counter = 0

    for line in students:
        if line["subject"].lower() == subject.lower():
            total += int(line["mark"])
            counter += 1
    if counter > 0:
        return total/counter
    else:
        return None

def top_student(students):
    highest_mark = 0
    name_of_student = ""
    subject = ""

    for line in students:
        if int(line["mark"]) > highest_mark:
            highest_mark = int(line["mark"])
            name_of_student = line["name"]
            subject = line["subject"]
    return highest_mark, name_of_student, subject

def show_subject(students, subject):
    subject_students = []

    for line in students:
        if line["subject"].lower() == subject.lower():
            subject_students.append(line)
    return subject_students

students = load_students("week10/practice_students.csv")


while True:
    print("\n---Menu---")
    print("\n1. Read file\n2. Choose student\n3. Choose subject\n4. Highest mark\n5. Average grade\n6. Add new student\n7. Top student\n8. Exit program")
 
    menu_choice = input("Enter a number: ").lower()
   
    if menu_choice == "1":
        shown_student = set()

        for line in students:
            student_identity = (line["name"], line["surname"])

            if student_identity not in shown_student:
                print(line["name"], line["surname"])
                shown_student.add(student_identity)

    elif menu_choice == "2":
        name_of_student = input("Enter name of student: ").lower()
        result = show_student(students, name_of_student)
        if result:
            print(name_of_student.title())

            for line in result:
                print(line["subject"], line["mark"])
        else:
            print("Student not found")

    elif menu_choice == "3":
        subject = input("Enter subject: ").lower()
        subject_result = show_subject(students, subject)

        if subject_result:
            print(f"\nStudents and marks for {subject.title()}:")

            for line in subject_result:
                print(line["name"], line["surname"], line["mark"])
        else:
            print("Subject not found")

    elif menu_choice == "4":
        subject = input("Enter subject: ").lower()
        result_highest_mark = highest_mark(students, subject)

        if result_highest_mark:
            mark, top_student_name = result_highest_mark
            print(f"{top_student_name} has the highest mark in {subject.title()}: {mark}")
        else:
            print("Subject not found")

    elif menu_choice == "5":
        subject = input("Enter subject: ").lower()
        average_result = average_grade(students, subject)

        if average_result is not None:
            print(f"The average grade for {subject.title()} is: {average_result:.2f}")
        else:
            print("Subject not found")

    elif menu_choice == "6":
        confirm_answer = input("Adding student... Enter yes to confirm: ").lower()
        if confirm_answer == "yes":
            new_name = input("Enter name: ")
            new_surname = input("Enter surname: ")
            new_subject = input("Enter subject: ")
            new_mark = input("Enter mark: ")
            add_student(students, new_name, new_surname, new_subject, new_mark)
            save_students("week10/practice_students.csv", students)

    elif menu_choice == "7":
        result_top = top_student(students)
        top_mark, top_name, top_subject = result_top

        print(f"{top_name} has the highest mark overall: {top_mark} in {top_subject}")

    elif menu_choice == "8":
        print("Exiting program")
        break

    else:
        print("Not a valid choice")