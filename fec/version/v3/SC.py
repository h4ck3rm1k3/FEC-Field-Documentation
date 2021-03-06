import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'NAME (Loan Source)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'ELECTION', 'number': '10'},
            {'name': 'ELECTION DESCRIPTION', 'number': '11'},
            {'name': 'ORIG. AMT OF LOAN', 'number': '12'},
            {'name': 'PAYMENT TO DATE', 'number': '13'},
            {'name': 'LOAN BALANCE', 'number': '14'},
            {'name': 'Incurred', 'number': '15-'},
            {'name': 'DUE DATE TERMS', 'number': '16'},
            {'name': 'PCT RATE TERMS', 'number': '17'},
            {'name': 'SECURED YESNO', 'number': '18'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '19'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '20'},
            {'name': 'CANDIDATE NAME', 'number': '21'},
            {'name': 'CAN/OFFICE', 'number': '22'},
            {'name': 'CAN/STATE', 'number': '23'},
            {'name': 'CAN/DIST', 'number': '24'},
            {'name': 'AMENDED CD', 'number': '25'},
            {'name': 'TRAN ID', 'number': '26'},
    ]
        self.fields_names = self.hash_names(self.fields)
