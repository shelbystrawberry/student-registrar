
#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Billing module for group 4 project
#

IN_TUITION = 25.00
OUT_TUITION = 850.00


def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    hours = 0
    for k, v in c_rosters:
        if id in v:
            hours += c_hours[k]
    if id in s_in_state:
        cost = hours * IN_TUITION
    else:
        cost = hours * OUT_TUITION
    return hours, cost


def display_hours_and_bill(hours, cost):
    print(f'Course load: {hours} credit hours\n'
          f'Enrollment cost: ${cost:.2f}')
