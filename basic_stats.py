# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/09/2023
# Description: Write a class called Student that has two private data members - the student's name and grade.
# Write a separate function called basic_stats that returns a tuple containing the mean, median, and
# mode of all the grades.
import statistics


class Student:
    """Represents a specific student with a grade."""

    def __init__(self, name, grade):
        self.__name = name  # name of student
        self.__grade = grade  # grade student received

    def get_grade(self):
        """returns the grade of the student."""
        return self.__grade


def basic_stats(student_list):
    """Function that will calculate the basic stats of the grades."""
    student_grades = []  # creates a list of grades for the students.

    for grade in student_list:
        student_grades.append(grade.get_grade())

    mean = statistics.mean(student_grades)
    median = statistics.median(student_grades)
    mode = statistics.mode(student_grades)
    stats = (mean, median, mode)
    return stats

# s1 = Student("Kyoungmin", 73)
# s2 = Student("Mercedes", 74)
# s3 = Student("Avanika", 78)
# s4 = Student("Marta", 74)

# student_list = [s1, s2, s3, s4]
# print(basic_stats(student_list))