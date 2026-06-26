# STUDENT RECORDS

student = {
    "Name": "Sajid Ali",
    "Roll No": "23p-3061",
    "Department": "Software Engineering",
    "Semester": "6th",
}

# COURSE RECORDS
courses = [
    (101, "Data Structure", 3, 67),
    (102, "Assembly ", 3, 80),
    (103, "Accounting", 2, 87),
    (104, "Islamiyat", 2, 93),
    (105, "Pak studies", 2, 96),
    (106, "Calculus", 2, 90),
]
# LIST OF THE CREDIT HOUSRS
credit_hour = []
for cr_h in courses:
    credit_hour.append(cr_h[2])

# GRADE
grade = []
for marks in courses:
    if marks[3] >= 90:
        grade.append(["A", 4.0])
    elif marks[3] >= 85:
        grade.append(["A-", 3.67])
    elif marks[3] >= 80:
        grade.append(["B+", 3.33])
    elif marks[3] >= 75:
        grade.append(["B", 3.00])
    elif marks[3] >= 70:
        grade.append(["B-", 2.67])
    elif marks[3] >= 65:
        grade.append(["C+", 2.33])
    elif marks[3] >= 60:
        grade.append(["C", 2.00])
    elif marks[3] >= 55:
        grade.append(["C-", 1.67])
    elif marks[3] >= 50:
        grade.append(["D", 1.33])
    else:
        grade.append(["F", 0])


# CALCULATE THE SEMESTER GPA AND RETURN IT
def semester_gpa():
    s_gpa = 0
    for c, g in zip(courses, grade):
        if g[0] != "F":
            s_gpa += (g[1] / 4.0) * c[2]
        else:
            s_gpa += 0
    return s_gpa


# GIVES US THE TOTAL CREADIT HOUSR A STUDENT HAS ATTEMPTED
def totlal_cr_h():
    cr_h = 0
    for cr in courses:
        cr_h += cr[2]
    return cr_h


# THIS WILL GIVE US THE EARNED CREDIT HOURS OF THE STUDENT
def earned_cr():
    er_c = 0
    for c, g in zip(courses, grade):
        if g[1] not in ("F", "f"):
            er_c += c[2]
    return er_c


# THIS FUNCTION WILL DISPLAY ALL THE TRANSCRIP
def display():
    print(
        "--------------------------------------------------------------------------------------------------------------"
    )
    print(
        f"Student Name:{student['Name']}\t\t\t\t\t\tDepartment Name:{student['Department']}"
    )
    print()
    print(
        f"Student RollNo:{student['Roll No']}\t\t\t\t\t\tCurrent Semester:{student['Semester']}"
    )
    print(
        "--------------------------------------------------------------------------------------------------------------"
    )
    print(
        "--------------------------------------------------------------------------------------------------------------"
    )
    print("course_id\t\tcourse_name\t\t\tcredit_hour\t\tgrade\t\t\tgpa")
    print(
        "--------------------------------------------------------------------------------------------------------------"
    )
    for i in range(6):
        print(
            f"{courses[i][0]}\t\t\t{courses[i][1]}\t\t\t{courses[i][2]}\t\t\t{grade[i][0]}\t\t\t{grade[i][1]}"
        )
    print(
        "--------------------------------------------------------------------------------------------------------------"
    )
    print(
        f"total credit hour:{totlal_cr_h()}\t\t\tearned credit hour:{earned_cr()}\t\t\t semester gpa:{semester_gpa()}"
    )
    print(
        "--------------------------------------------------------------------------------------------------------------"
    )


display()
