#
# Benjamin Nicholson / Selby Sanchez-Herrera
# 12/05/2021
# initialize data files to default
#

import pickle

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


def main():
    file = open('data.dat', 'wb')
    pickle.dump(student_list, file)
    pickle.dump(student_in_state, file)
    pickle.dump(course_hours, file)
    pickle.dump(course_roster, file)
    pickle.dump(course_max_size, file)
    file.close()


main()
