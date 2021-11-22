#
# Benjamin Nicholson / Shelby Sanchez-Herrera
# 12/05/2021
# Billing module for group 4 project
#

IN_TUITION = 225.00
OUT_TUITION = 850.00


class Billing:
    def __init__(self, id, s_in_state, c_rosters, c_hours):
        self.hours = 0
        self.cost = 0
        self.__id = id
        self.__s_in_state = s_in_state
        self.__c_rosters = c_rosters
        self.__c_hours = c_hours

    def calculate_hours_and_bill(self):
        in_state = False

        # Go through Roster dictionary and look for enrollment.
        # If enrolled in course, find credit hours for course and
        # add to total credit hours student is taking.
        for key in self.__c_rosters:
            if self.__id in self.__c_rosters[key]:
                for k in self.__c_hours:
                    if key == k:
                        self.hours += self.__c_hours[k]

        # Check if student is an instate student.
        # Assigns True or False to variable 'in_state' depending on instate status.
        for student in self.__s_in_state:
            if self.__id == student:
                in_state = self.__s_in_state[student]

        # Out of state tuition calculation
        if not in_state:
            self.cost = self.hours * OUT_TUITION

        # In state tuition calculation
        else:
            self.cost = self.hours * IN_TUITION

        # returns values for total credit hours and total tuition cost in that order
        # return self.hours, self.cost

    # Uses an f string to present student bill
    def __str__(self):
        return f'Course load: {self.hours} credit hours\n' \
               f'Enrollment cost: ${self.cost:.2f}'
