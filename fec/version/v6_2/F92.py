import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID NUMBER', 'number': '4'},
            {'name': 'BACK REFERENCE SCHED NAME', 'number': '5'},
            {'name': 'ENTITY TYPE', 'number': '6'},
            {'name': 'DONOR ORGANIZATION NAME', 'number': '7'},
            {'name': 'DONOR LAST NAME', 'number': '8'},
            {'name': 'DONOR FIRST NAME', 'number': '9'},
            {'name': 'DONOR MIDDLE NAME', 'number': '10'},
            {'name': 'DONOR PREFIX', 'number': '11'},
            {'name': 'DONOR SUFFIX', 'number': '12'},
            {'name': 'DONOR STREET 1', 'number': '13'},
            {'name': 'DONOR STREET 2', 'number': '14'},
            {'name': 'DONOR CITY', 'number': '15'},
            {'name': 'DONOR STATE', 'number': '16'},
            {'name': 'DONOR ZIP', 'number': '17'},
            {'name': 'DATE RECEIVED', 'number': '18'},
            {'name': 'AMOUNT RECEIVED', 'number': '19'},
    ]
        self.fields_names = self.hash_names(self.fields)
