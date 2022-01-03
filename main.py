student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇


def convert(my_dictionary):
    for student in my_dictionary:
        if my_dictionary[student] in range(91, 101):
            student_grades[student] = "Outstanding"
        elif my_dictionary[student] in range(81, 91):
            student_grades[student] = "Exceeds Expectations"
        elif my_dictionary[student] in range(71, 81):
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"


convert(student_scores)


# 🚨 Don't change the code below 👇
print(student_grades)
