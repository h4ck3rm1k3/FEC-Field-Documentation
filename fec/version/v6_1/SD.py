import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ENTITY TYPE', 'number': '4'},
            {'name': 'CREDITOR ORGANIZATION NAME', 'number': '5'},
            {'name': 'CREDITOR LAST NAME', 'number': '6'},
            {'name': 'CREDITOR FIRST NAME', 'number': '7'},
            {'name': 'CREDITOR MIDDLE NAME', 'number': '8'},
            {'name': 'CREDITOR PREFIX', 'number': '9'},
            {'name': 'CREDITOR SUFFIX', 'number': '10'},
            {'name': 'CREDITOR STREET 1', 'number': '11'},
            {'name': 'CREDITOR STREET 2', 'number': '12'},
            {'name': 'CREDITOR CITY', 'number': '13'},
            {'name': 'CREDITOR STATE', 'number': '14'},
            {'name': 'CREDITOR ZIP', 'number': '15'},
            {'name': 'PURPOSE OF DEBT OR OBLIGATION', 'number': '16'},
            {'name': 'BEGINNING BALANCE (This Period)', 'number': '17'},
            {'name': 'INCURRED AMOUNT (This Period)', 'number': '18'},
            {'name': 'PAYMENT AMOUNT (This Period)', 'number': '19'},
            {'name': 'BALANCE AT CLOSE (This Period)', 'number': '20'},
    ]
        self.fields_names = self.hash_names(self.fields)
