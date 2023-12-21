class PAQ:
    def __init__(self, name, field, empID, employed):
        self.name = name
        self.field = field
        self.empID = empID
        self.employed = employed

    def paqUpdateList(self, dodID, name, field, empID, employed):
        [dodID] = PAQ(dodID, name, field, empID, employed)
