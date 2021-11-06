#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Billing module for group 4 project
#

IN_TUITION = 225.00
OUT_TUITION = 850.00


def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    hours = 0
    cost = 0
    in_state = False
    for key in c_rosters:
        # v = c_hours[key]
        if id in c_rosters[key]:
            for k in c_hours:
                if key == k:
                    hours += c_hours[k]

    for student in s_in_state:
        if id == student:
            # cost = hours * IN_TUITION
            # skip = True
            # break
            in_state = s_in_state[student]

    if not in_state:
        cost = hours * OUT_TUITION
    else:
        cost = hours * IN_TUITION

    return hours, cost


def display_hours_and_bill(hours, cost):
    print(f'Course load: {hours} credit hours\n'
          f'Enrollment cost: ${cost:.2f}')
