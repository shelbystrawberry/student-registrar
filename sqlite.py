#
# Benjamin Nicholson / Selby Sanchez-Herrera
# 12/05/2021
# Read and write data to sqlite db
#

import json
import sqlite3

import salt


def create():
    con = sqlite3.connect('registrar.db')
    cur = con.cursor()

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

    try:
        cur.execute('''CREATE TABLE salted_student_list(id TEXT, salt TEXT, pin TEXT)''')
        cur.execute('''CREATE TABLE student_in_state(id TEXT, bool INTEGER)''')
        cur.execute('''CREATE TABLE course_hours(class TEXT, hours INTEGER)''')
        cur.execute('''CREATE TABLE course_roster(class TEXT, students TEXT)''')
        cur.execute('''CREATE TABLE course_max_size(class TEXT, size INTEGER)''')
    except sqlite3.OperationalError:
        pass

    for element in salted_student_list:
        cur.execute(
            f"INSERT INTO salted_student_list (id, salt, pin) VALUES (?, ?, ?)",
            (element[0], element[1], element[2])
        )

    for key in student_in_state:
        cur.execute(
            f"INSERT INTO student_in_state (id, bool) VALUES (?, ?)",
            (key, int(student_in_state[key]))
        )

    for key in course_hours:
        cur.execute(
            f"INSERT INTO course_hours (class, hours) VALUES (?, ?)",
            (key, course_hours[key])
        )

    for key in course_roster:
        cur.execute(
            f"INSERT INTO course_roster (class, students) VALUES (?, ?)",
            (key, json.dumps(course_roster[key]))
        )

    for key in course_max_size:
        cur.execute(
            f"INSERT INTO course_max_size (class, size) VALUES (?, ?)",
            (key, course_max_size[key])
        )

    con.commit()
    con.close()
