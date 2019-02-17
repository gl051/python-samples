"""
    Generic Indivividual
"""


class Individual(object):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
            self.gender = 'N/A'

        def fullname(self):
            return f'{self.firstname} {self.lastname}'
