from individual import Individual


class Teacher(Individual):
    """ A teacher is an individual """
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self._subject = subject

    """ Override the parent method """
    def fullname(self):
        return f'{self.lastname}, {self.firstname} teaches {self._subject}'
