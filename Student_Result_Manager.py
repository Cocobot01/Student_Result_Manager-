student = {}

while True:
    print("\n-----Student Manager App----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    #Add Student
    if choice=="1":
        name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")
        student[name]= marks
        print(f"{name} Sucessfully added!!")
        
    #View Student
    elif choice=="2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name,":",marks)
                
    #Check Result
    elif choice=="3":
        name = input("Enter student name: ")
        if name in student:
            marks = student[name]
            
            if marks>="40":
                print("Pass")
            else:
                print("Sorry Fail")
        else:
            print("Student NOT Found!!")
            
    #Exit
    elif choice=="4":
        print("Exiting......")
        break

    else:
        print("Invalid input")
    
