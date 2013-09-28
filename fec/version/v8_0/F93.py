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
            {'name': 'PAYEE ORGANIZATION NAME', 'number': '7'},
            {'name': 'PAYEE LAST NAME', 'number': '8'},
            {'name': 'PAYEE FIRST NAME', 'number': '9'},
            {'name': 'PAYEE MIDDLE NAME', 'number': '10'},
            {'name': 'PAYEE PREFIX', 'number': '11'},
            {'name': 'PAYEE SUFFIX', 'number': '12'},
            {'name': 'PAYEE STREET 1', 'number': '13'},
            {'name': 'PAYEE STREET 2', 'number': '14'},
            {'name': 'PAYEE CITY', 'number': '15'},
            {'name': 'PAYEE STATE', 'number': '16'},
            {'name': 'PAYEE ZIP', 'number': '17'},
            {'name': 'ELECTION CODE', 'number': '18'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '19'},
            {'name': 'EXPENDITURE DATE', 'number': '20'},
            {'name': 'EXPENDITURE AMOUNT', 'number': '21'},
            {'name': 'EXPENDITURE PURPOSE DESCRIP', 'number': '22'},
            {'name': 'PAYEE EMPLOYER', 'number': '23'},
            {'name': 'PAYEE OCCUPATION', 'number': '24'},
            {'name': 'COMMUNICATION DATE', 'number': '25'},
    ]
        self.fields_names = self.hash_names(self.fields)
