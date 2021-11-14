import hashlib
import random
import string


initial_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]

salted_student_list = []


def create_users(s_list):
    for t in s_list:
        add_user(t[0], t[1])
    return salted_student_list


def load_users(user_tuples):
    for user in user_tuples:
        store(user[0], user[1], user[2])


def add_user(username, password):
    salt = make_salt(32)
    hash_brown = hash_pass(password, salt)
    store(username, salt, hash_brown)


def make_salt(num):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(num))


def hash_pass(password, salt):
    salted_pass = salt + password
    return hashlib.sha256(salted_pass.encode()).hexdigest()


def store(user, salt, password):
    salted_student_list.append((user, salt, password))
    # print(user, salt, password)


def check_user(username, password):
    user_entry = [user_item for user_item in salted_student_list if user_item[0] == username]
    if user_entry:
        salt = user_entry[0][1]
        hashed_pass = hash_pass(password, salt)
        return user_entry[0][2] == hashed_pass
    else:
        return False
