#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Main module for group 4 project
#

import pickle

import salt
from billing import Billing
from student import Student
from admin import *


salted_student_list = []
student_in_state = {}
course_hours = {}
course_roster = {}
course_max_size = {}
deactivated_users = []


def login(id):
    active_user = True
    # Check for exit condition
    if id == '0':
        exit(0)

    # get user pin and create tuple to compare
    log_in_pin = input('Enter PIN: ')

    login_valid = salt.check_user(id, log_in_pin)
    if id in deactivated_users:
        active_user = False
    if login_valid and active_user:
        print('ID and PIN verified')
        return login_valid
    else:
        print('ID or PIN incorrect')



def access_data():
    global salted_student_list, student_in_state, course_hours, course_roster, course_max_size, deactivated_users
    try:
        file = open('data.dat', 'rb')
        salted_student_list = pickle.load(file)
        student_in_state = pickle.load(file)
        course_hours = pickle.load(file)
        course_roster = pickle.load(file)
        course_max_size = pickle.load(file)
        deactivated_users = pickle.load(file)
        file.close()
        salt.load_users(salted_student_list)
    except FileNotFoundError:
        student_list = [('admin', 'admin'),
                        ('1001', '111'),
                        ('1002', '222'),
                        ('1003', '333'),
                        ('1004', '444'),
                        ]

        salted_student_list = salt.create_users(student_list)

        student_in_state = {'1001': True,
                            '1002': False,
                            '1003': True,
                            '1004': False}

        course_hours = {'CSC101': 3,
                        'CSC102': 4,
                        'CSC103': 5,
                        'CSC104': 3}
        course_roster = {'CSC101': ['1004', '1003'],
                         'CSC102': ['1001'],
                         'CSC103': ['1002'],
                         'CSC104': []}
        course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}


def write_data():
    global salted_student_list, student_in_state, course_hours, course_roster, course_max_size, deactivated_users
    file = open('data.dat', 'wb')
    pickle.dump(salted_student_list, file)
    pickle.dump(student_in_state, file)
    pickle.dump(course_hours, file)
    pickle.dump(course_roster, file)
    pickle.dump(course_max_size, file)
    pickle.dump(deactivated_users, file)
    file.close()
    print('Data saved to data.dat')


def add_new_student():
    global salted_student_list, student_in_state, course_hours, course_roster, course_max_size
    if len(salted_student_list) < 10:
        p = '100'
    elif len(salted_student_list) < 100:
        p = '10'
    elif len(salted_student_list) < 1000:
        p = '1'
    new_id = p + str(len(salted_student_list))
    print(f'Your student ID will be {new_id}.')
    match = False
    new_pin = ''
    while not match:
        pin1 = input('Enter new PIN: ')
        pin2 = input('Re-enter PIN: ')
        if pin1 == pin2:
            new_pin = pin1
            match = True
        else:
            print("PIN's do not match.")
    salted_student_list = salt.add_user(new_id, new_pin)
    try:
        in_state = input('Have you lived in North Carolina for the past 6 months? Y/N: ')
        if in_state.upper() == 'Y':
            student_in_state[new_id] = True
        elif in_state.upper() == 'N':
            student_in_state[new_id] = False
        else:
            raise ValueError
    except ValueError:
        print('Invalid entry')
    write_data()


def main():
    global salted_student_list, student_in_state, course_hours, course_roster, course_max_size, deactivated_users
    logged_in = False
    admin = False
    access_data()
    while not logged_in and not admin:

        id = input('Enter ID to log in, C to create new account, or 0 to quit: ')
        if id == 'admin':
            admin = login(id)
        elif id.upper() == 'C':
            add_new_student()
        else:
            logged_in = login(id)

        # Continue offering selection menu until verified user exits.
        while logged_in:
            menu = input('Enter 1 to add course, 2 to drop course, '
                         '3 to list courses, 4 to show bill, 5 to view available courses or 0 to exit: ')

            student = Student(id, course_roster, course_max_size)
            if menu == '1':
                # add_course(id, course_roster, course_max_size)
                student.add_course()

            elif menu == '2':
                # drop_course(id, course_roster)
                student.drop_course()

            elif menu == '3':
                # list_courses(id, course_roster)
                student.list_courses()

            elif menu == '4':
                bill = Billing(id, student_in_state, course_roster, course_hours)
                bill.calculate_hours_and_bill()
                print(bill)

            elif menu == '5':
                student.view_courses()

            elif menu == '0':
                write_data()
                logged_in = False

            else:
                print('Invalid Choice')

            # Admin utilities
        while admin:
            menu = input('Enter 1 to create new course, 2 to delete existing course, '
                         '3 to drop student from course, 4 to delete student, '
                         '5 to list all students, 0 to exit: ')

            if menu == '1':
                create_course(course_hours, course_roster, course_max_size)
                write_data()

            elif menu == '2':
                delete_course(course_hours, course_roster, course_max_size)
                write_data()

            elif menu == '3':
                drop_student(course_roster)
                write_data()

            elif menu == '4':
                deactivate_student(deactivated_users)
                write_data()

            elif menu == '5':
                list_students(salted_student_list)

            elif menu == '0':
                write_data()
                admin = False


main()
