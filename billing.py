#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Billing module for group 4 project
#

IN_TUITION = 225.00
OUT_TUITION = 850.00


def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    hours = 0
    in_state = False

    # Go through Roster dictionary and look for enrollment.
    # If enrolled in course, find credit hours for course and
    # add to total credit hours student is taking.
    for key in c_rosters:
        if id in c_rosters[key]:
            for k in c_hours:
                if key == k:
                    hours += c_hours[k]

    # Check if student is an instate student.
    # Assigns True or False to variable 'in_state' depending on instate status.
    for student in s_in_state:
        if id == student:
            in_state = s_in_state[student]

    # Out of state tuition calculation
    if not in_state:
        cost = hours * OUT_TUITION

    # In state tuition calculation
    else:
        cost = hours * IN_TUITION

    # returns values for total credit hours and total tuition cost in that order
    return hours, cost


def display_hours_and_bill(hours, cost):

    # Uses an f string to present student bill
    print(f'Course load: {hours} credit hours\n'
          f'Enrollment cost: ${cost:.2f}')
