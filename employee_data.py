global paq_Arr


class PAQ:
    def __init__(self, name, field, empID, employed):
        self.name = name
        self.field = field
        self.empID = empID
        self.employed = employed
        # self.dodID = dodID

    def paqUpdateList(self):
        paq_Arr = {}
        newPAQ = PAQ(self.name, self.field, self.empID, self.employed)
        paq_Arr[self.empID] = newPAQ
