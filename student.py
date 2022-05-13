#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Student module
#

class Student:
    def __init__(self, id, c_roster, c_maxsize):
        self.id = id
        self.c_roster = c_roster
        self.c_maxsize = c_maxsize

    def add_course(self):
        course_input = (input('Enter the course you\'d like to add: ')).upper()
        if course_input not in self.c_roster:
            print('Please enter a valid course.')
        else:
            if self.id in self.c_roster[course_input]:
                print('Already Enrolled.')
            else:
                if len([item for item in self.c_roster[course_input]]) >= self.c_maxsize[course_input]:
                    print('Course is at full capacity.')
                else:
                    self.c_roster[course_input].append(self.id)
                    print(f'Course {course_input} was added.')

    def drop_course(self):
        course_input = input('Enter the course you\'d like to drop: ').upper()
        if course_input not in self.c_roster:
            print('Please enter a valid course.')
        else:
            if self.id not in self.c_roster[course_input]:
                print('You are not enrolled in that class.')
            else:
                for i in self.c_roster[course_input]:
                    if i == self.id:
                        index = list(self.c_roster[course_input]).index(f'{self.id}')
                        del self.c_roster[course_input][index]
                print(f'Class {course_input} was dropped.')

    def list_courses(self):
        course_count = 0
        course_list = []
        for i in self.c_roster:
            for j in self.c_roster[i]:
                if self.id == j:
                    course_count += 1
                    course_list.append(i)
        print('Courses Registered:')
        for i in course_list:
            print(i)
        print(f'Total number: {course_count}')

    def view_courses(self):
        print('Course List and their Available Seats')
        for key_r in self.c_roster:
            print(f'{key_r}: {int(self.c_maxsize[key_r]) - len(self.c_roster[key_r])}')
