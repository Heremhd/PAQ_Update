paq_Arr = {}


class PAQ:

    def __init__(self, name, field, empID, employed):
        self.name = name
        self.field = field
        self.empID = empID
        self.employed = employed
        # self.dodID = dodID
        paq_Arr[self.empID] = self
