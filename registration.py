#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Main module for group 4 project
#

from student import add_course, drop_course, list_courses
from billing import calculate_hours_and_bill, display_hours_and_bill


def login(id, s_list):
    # Check for exit condition
    if id == '0':
        exit(0)

    # get user pin and create tuple to compare
    # *** POSSIBLE EC OPPORTUNITY ***
    # Consider proposal to encrypt user pin for security -Discuss in future
    log_in_pin = input('Enter PIN: ')
    log_in = (id, log_in_pin)

    # Verify ID and PIN
    if log_in in s_list:
        print('ID and PIN verified')
        return True
    else:
        print('ID or PIN incorrect')
        return False


def write_data(student_list, student_in_state, course_hours, course_roster, course_max_size):
    file = open('data.dat', 'wb')
    pickle.dump(student_list, file)
    pickle.dump(student_in_state, file)
    pickle.dump(course_hours, file)
    pickle.dump(course_roster, file)
    pickle.dump(course_max_size, file)
    file.close()
    print('Data saved to data.dat')


def main():
    # Prerequisite data
    # *** POSSIBLE EC OPPORTUNITY ***
    # Consider moving all data to a info.dat file system
    # and implement the pickle method for data management. -Discuss in future
    # student_list = [('1001', '111'), ('1002', '222'),
    #                 ('1003', '333'), ('1004', '444')]
    # 
    # student_in_state = {'1001': True,
    #                     '1002': False,
    #                     '1003': True,
    #                     '1004': False}
    # 
    # course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    # course_roster = {'CSC101': ['1004', '1003'],
    #                  'CSC102': ['1001'],
    #                  'CSC103': ['1002'],
    #                  'CSC104': []}
    # course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    logged_in = False
    menu = ""
    file = open('data.dat', 'rb')
    student_list = pickle.load(file)
    student_in_state = pickle.load(file)
    course_hours = pickle.load(file)
    course_roster = pickle.load(file)
    course_max_size = pickle.load(file)
    file.close()

    # Continue asking user to login or exit until success at either one.
    while not logged_in:
        id = input('Enter ID to log in, or 0 to quit: ')
        logged_in = login(id, student_list)

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
                hours, cost = calculate_hours_and_bill(id, student_in_state, course_roster, course_hours)
                display_hours_and_bill(hours, cost)

            elif menu == '0':
                write_data(student_list, student_in_state, course_hours, course_roster, course_max_size)
                logged_in = False

            else:
                print('Invalid Choice')


main()
