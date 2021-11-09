#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Student module for group 4 project
#


def add_course(id, c_roster, c_max_size):
    course_input = (input('Enter the course you\'d like to add: ')).upper()
    if course_input not in c_roster:
        print('Please enter a valid course.')
    else:
        if id in c_roster[course_input]:
            print('Already Enrolled.')
        else:
            if len([item for item in c_roster[course_input]]) >= c_max_size[course_input]:
                print('Course is at full capacity.')
            else:
                c_roster[course_input].append(id)
                print(f'Course {course_input} was added.')


def drop_course(id, c_roster):
    course_input = input('Enter the course you\'d like to drop: ')
    if course_input not in c_roster:
        print('Please enter a valid course.')
    else:
        if id not in c_roster[course_input]:
            print('You are not enrolled in that class.')
        else:
            for i in c_roster[course_input]:
                if i == id:
                    index = list(c_roster[course_input]).index(f'{id}')
                    del c_roster[course_input][index]
            print(f'Class {course_input} was dropped.')


def list_courses(id, c_roster):
    course_count = 0
    course_list = []
    for i in c_roster:
        for j in c_roster[i]:
            if id == j:
                course_count += 1
                course_list.append(i)
    print('Courses Registered:')
    for i in course_list:
        print(i)
    print(f'Total number: {course_count}')
