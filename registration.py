#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Main module for group 4 project
#

from student import add_course, drop_course, list_courses
from billing import calculate_hours_and_bill, display_hours_and_bill


def login(id, s_list):
    if id == '0':
        exit(0)
    log_in_pin = input('Enter PIN: ')
    log_in = (id, log_in_pin)
    if log_in in s_list:
        print('ID and PIN verified')
        return True
    else:
        print('ID or PIN incorrect')
        return False


def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    logged_in = False
    menu = ''

    while not logged_in:
        id = input('Enter ID to log in, or 0 to quit: ')
        logged_in = login(id, student_list)

    while menu != '0':
        menu = input('Enter 1 to add course, 2 to drop course, '
                     '3 to list courses, 4 to show bill, 0 to exit: ')

        if menu == '1':
            ...

        elif menu == '2':
            ...

        elif menu == '3':
            ...

        elif menu == '4':
            hours, cost = calculate_hours_and_bill(id, student_in_state,
                                                   course_roster, course_hours)
            display_hours_and_bill(hours, cost)

        elif menu == '0':
            exit(0)

        else:
            print('Invalid Choice')


main()
