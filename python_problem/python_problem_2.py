#함수 이름은 변경 가능합니다.

students = {}

##############  menu 1
def Menu1(name, mid_score, final_score) :
    #사전에 학생 정보 저장하는 코딩 
    students[name] = {"mid": mid_score, "final": final_score, "grade": None}

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for name, info in students.items():
        if info["grade"] is None:
            average = (info["mid"] + info["final"]) / 2
            if average >= 90:
                info["grade"] = "A"
            elif average >= 80:
                info["grade"] = "B"
            elif average >= 70:
                info["grade"] = "C"
            else:
                info["grade"] = "D"
        print("Grading to all students.")


##############  menu 3
def Menu3():
    print("-------------------------------")
    print("name    mid    final    grade")
    print("-------------------------------")
    for name, info in students.items():
        print(f"{name:<8}{info['mid']:<8}{info['final']:<8}{info['grade']}")
    print("-------------------------------")


##############  menu 4
def Menu4(name):
    del students[name]
    print(f"{name} student information is deleted.")


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        data = input("Enter name mid-score final-score : ").split()
        if len(data) != 3:
            print("Num of data is not 3!")
            continue
        name, mid, final = data
        if name in students:
            print("Already exist name!")
            continue
        if not mid.isdigit() or not final.isdigit():
            print("Score is not positive integer!")
            continue
        Menu1(name, int(mid), int(final))


    elif choice == "2":
        if not students:
            print("No student data!")
            continue
        Menu2()


    elif choice == "3":
        if not students:
            print("No student data!")
            continue
        if any(info["grade"] is None for info in students.values()):
            print("There is a student who didn't get grade.")
            continue
        Menu3()


    elif choice == "4":
        if not students:
            print("No student data!")
            continue
        name_to_delete = input("Enter the name to delete : ")
        if name_to_delete not in students:
            print("Not exist name!")
            continue
        Menu4(name_to_delete)


    elif choice == "5" :
        print("Exit Program!")
        break

    else :
        print("Wrong number.Choose again")