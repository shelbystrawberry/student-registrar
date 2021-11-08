#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Student module for group 4 project
#


def add_course(id, c_roster, c_max_size):
    course_added = False
    while not course_added:
        course_input = input('Enter the course you\'d like to add: ')
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
                    course_added = True


def drop_course(id, c_roster):
    ...


def list_courses(id, c_roster):
    ...
