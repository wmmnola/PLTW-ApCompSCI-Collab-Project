"""Card object"""
# Card Object


class Card(object):
    def __init__(self, id, passedvalue):
        self.id = id
        self.passed_value = passedvalue

    def get_real_value(self):
        if self.passed_value >= 11:
            self.real_value = 10
        else:
            self.real_value = self.passed_value
