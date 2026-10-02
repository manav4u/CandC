students = []
def add_student():
    print("Add Student : ")
    name= input("Student Name :")
    roll = int(input("Roll Number : "))
    marks = float(input("Marks : "))

    student = {
        "name" : name,
        "roll":roll,
        "marks": marks
    }
    students.append(student)
def view_student():
    for s in students:
        print("Name : ",s['name'])
        print("Roll : ",s['roll'])
        print("Marks : ",s['marks'])

def calculate_result():
    for s in students:
        marks = s['marks']
        if marks > 85:
            result = "A"

        elif marks < 85 and marks > 75:
            result = "B"

        elif marks < 75 and marks > 55:
            result = "C"
        else:
            result = "Fail"

        print("Name : ",s['name'])
        print("Roll : ",s['roll'])
        print("Marks : ",marks)
        print("Result : ",result)

def main():
    while True:

        print("\n[green]==============================[green]")
        print("  STUDENT PERFORMANCE ANALYZER")
        print("[green]==============================[green]")

        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Result")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            calculate_result()

        elif choice == "4":
            print("Thank you for using Student Analyzer!")
            break

        else:
            print("Invalid choice. Try again.")


main()