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
            {'name': 'CONTRIBUTOR ORGANIZATION NAME', 'number': '7'},
            {'name': 'CONTRIBUTOR LAST NAME', 'number': '8'},
            {'name': 'CONTRIBUTOR FIRST NAME', 'number': '9'},
            {'name': 'CONTRIBUTOR MIDDLE NAME', 'number': '10'},
            {'name': 'CONTRIBUTOR PREFIX', 'number': '11'},
            {'name': 'CONTRIBUTOR SUFFIX', 'number': '12'},
            {'name': 'CONTRIBUTOR STREET 1', 'number': '13'},
            {'name': 'CONTRIBUTOR STREET 2', 'number': '14'},
            {'name': 'CONTRIBUTOR CITY', 'number': '15'},
            {'name': 'CONTRIBUTOR STATE', 'number': '16'},
            {'name': 'CONTRIBUTOR ZIP', 'number': '17'},
            {'name': 'DONATION DATE', 'number': '18'},
            {'name': 'DONATION AMOUNT', 'number': '19'},
            {'name': 'DONATION AGGREGATE AMOUNT', 'number': '20'},
            {'name': 'MEMO CODE', 'number': '21'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '22'},
    ]
        self.fields_names = self.hash_names(self.fields)
