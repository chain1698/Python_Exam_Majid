def check_grades(grades):
    for grade in grades:
        if grade >= 75:
            print("Pass")
        else:
            print("No")

tets_grades = [50, 45, 75, 55, 30]
check_grades(tets_grades)