#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Admin module for group 4 project
#


def create_course(course_hours, course_roster, course_max_size):
    course_name = input('Enter course name: ')
    credit_hours = int(input('Enter credit hours for course: '))
    seats = int(input('Enter number of available seats: '))

    course_hours[course_name.upper()] = credit_hours
    course_roster[course_name.upper()] = []
    course_max_size[course_name.upper()] = seats
    print(f'{course_name.upper()} has been created with {seats} '
          f'seats and worth {credit_hours} credit hours.')


def delete_course(course_hours, course_roster, course_max_size):
    ru_sure = input('WARNING! YOU ARE ABOUT TO DELETE ALL REGISTERED STUDENTS FROM A COURSE.\n'
                    'THIS ACTION IS IRREVERSIBLE. MAKE SURE YOU KNOW WHAT YOU ARE DOING BEFORE\n'
                    'PROCEEDING! TYPE "YES" TO CONTINUE: ')
    if ru_sure == 'YES':
        course = input('Enter course to be removed: ')
        try:
            course_hours = course_hours.pop(course.upper())
            course_roster = course_roster.pop(course.upper())
            course_max_size = course_max_size.pop(course.upper())
            print(f'{course.upper()} has been removed.')
        except KeyError:
            print('Course does not exist.')

    else:
        print('Returning to menu. No changes were made.')


def drop_student(course_roster):
    course = input('Please enter course: ')
    stu = input('Please enter student ID: ')

    print(f'Warning! You are about to remove student {stu} from {course}.')
    ru_sure = input('Do you wish to proceed? Y/N: ')

    if ru_sure.upper() == 'Y':
        if course in course_roster:
            if stu in course_roster[course]:
                temp_list = course_roster.pop(course)
                temp_list.remove(stu)
                course_roster[course] = temp_list
                print(f'Student {stu} removed from {course}')
            else:
                print(f'Student {stu} not in {course}')

        else:
            print(f'{course} not found.')

    else:
        print('Returning to menu. No changes were made.')


def deactivate_student(deactivated_users):
    stu = input('Enter Student ID to be deactivated: ')
    deactivated_users.append(stu)
    print(deactivated_users)


def list_students(salted_student_list):
    for student in salted_student_list:
        print(student[0])
