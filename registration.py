#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Main module for group 4 project
#

from student import add_course, drop_course, list_courses
from billing import Billing
import pickle
import salt


def login(id, s_list):
    # # Check for exit condition
    if id == '0':
        exit(0)
    #
    # # get user pin and create tuple to compare
    log_in_pin = input('Enter PIN: ')

    login_valid = salt.check_user(id, log_in_pin)
    if login_valid:
        print('ID and PIN verified')
    else:
        print('ID or PIN incorrect')

    return login_valid


def access_data():
    try:
        file = open('data.dat', 'rb')
        salted_student_list = pickle.load(file)
        student_in_state = pickle.load(file)
        course_hours = pickle.load(file)
        course_roster = pickle.load(file)
        course_max_size = pickle.load(file)
        file.close()
        salt.load_users(salted_student_list)
    except FileNotFoundError:
        student_list = [('1001', '111'), ('1002', '222'),
                        ('1003', '333'), ('1004', '444')]

        salted_student_list = salt.create_users(student_list)

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

    return salted_student_list, student_in_state, course_hours, course_roster, course_max_size


def write_data(salted_student_list, student_in_state, course_hours, course_roster, course_max_size):
    file = open('data.dat', 'wb')
    pickle.dump(salted_student_list, file)
    pickle.dump(student_in_state, file)
    pickle.dump(course_hours, file)
    pickle.dump(course_roster, file)
    pickle.dump(course_max_size, file)
    file.close()
    print('Data saved to data.dat')


def main():
    logged_in = False
    menu = ""
    salted_student_list, student_in_state, course_hours, course_roster, course_max_size = access_data()
    while not logged_in:
        id = input('Enter ID to log in, or 0 to quit: ')
        logged_in = login(id, salted_student_list)

        # Continue offering selection menu until verified user exits.
        while logged_in:
            menu = input('Enter 1 to add course, 2 to drop course, '
                         '3 to list courses, 4 to show bill, 0 to exit: ')

            if menu == '1':
                add_course(id, course_roster, course_max_size)

            elif menu == '2':
                drop_course(id, course_roster)

            elif menu == '3':
                list_courses(id, course_roster)

            elif menu == '4':
                bill = Billing(id, student_in_state, course_roster, course_hours)
                bill.calculate_hours_and_bill()
                print(bill)

            elif menu == '0':
                write_data(salted_student_list, student_in_state, course_hours, course_roster, course_max_size)
                logged_in = False

            else:
                print('Invalid Choice')


main()
